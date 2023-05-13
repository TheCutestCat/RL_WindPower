from floris.tools import FlorisInterface
import numpy as np
from matplotlib import pyplot as plt
from floris.tools.visualization import visualize_cut_plane

class env():
    def __init__(self):
        # 1. Load an input file
        self.fi = FlorisInterface("inputs/gch.yaml")

        # 2. Modify the inputs with a more complex wind turbine layout
        D = 126.0  # Design the layout based on turbine diameter

        x = [0, 0,  6 * D, 6 * D, 12*D,12*D]
        y = [0, 3 * D, 0, 3 * D,0,3*D]
        self.wind_directions = [270.0]
        wind_speeds = [8.0]
        self.farm_power_baseline = None
        self.farm_power_yaw = None
        self.yaw_angles = None
        # Pass the new data to FlorisInterface
        self.fi.reinitialize(
            layout_x=x,
            layout_y=y,
            wind_directions=self.wind_directions,
            wind_speeds=wind_speeds
        )

    def CalculateNonYaw(self):
        # 3. Calculate the velocities at each turbine for all atmospheric conditions
        # All turbines have 0 degrees yaw
        self.fi.calculate_wake()
        # 4. Get the total farm power
        turbine_powers = self.fi.get_turbine_powers() / 1000.0  # Given in W, so convert to kW
        self.farm_power_baseline = np.sum(turbine_powers, 2)  # Sum over the third dimension

    def SetYawAngle(self,Angle):
        # angle 一个一维数组 len = 6
        # 5. Develop the yaw control settings
        if(len(Angle)!=6):
            raise ValueError('len of Angle should be 6')
        self.yaw_angles = np.zeros( (1, 1, 6) )  # Construct the yaw array with dimensions for two wind directions, one wind speed, and four turbines
        for i in range(len(Angle)):
            if(not isinstance(Angle[i],(float,int)) or Angle[i]>70 or Angle[i]<-70):
                raise ValueError('Angle should be float and in the section of [-70,70]')
            self.yaw_angles[0, :, i] = Angle[i]
    def CalculateWithYaw(self):
        # 6. Calculate the velocities at each turbine for all atmospheric conditions with the new yaw settings
        self.fi.calculate_wake(yaw_angles=self.yaw_angles)

        # 7. Get the total farm power
        turbine_powers = self.fi.get_turbine_powers() / 1000.0
        self.farm_power_yaw = np.sum(turbine_powers, 2)
        # 8. Compare farm power with and without wake steering
        difference = 100 * (self.farm_power_yaw - self.farm_power_baseline) / self.farm_power_baseline
        print("Power % difference with yaw")
        print(f"    270 degrees: {difference[0, 0]:4.2f}%")
        return difference
    def show(self):

        fig, axarr = plt.subplots(2, 1, figsize=(15,8))

        horizontal_plane = self.fi.calculate_horizontal_plane(wd=[self.wind_directions[0]], height=90.0)
        visualize_cut_plane(horizontal_plane, ax=axarr[0], title="270 - Aligned")

        horizontal_plane = self.fi.calculate_horizontal_plane(wd=[self.wind_directions[0]], yaw_angles=self.yaw_angles[0:1,0:1] , height=90.0)
        visualize_cut_plane(horizontal_plane, ax=axarr[1], title="270 - Yawed")

        plt.show()

myenv = env()
myenv.CalculateNonYaw()
myenv.SetYawAngle(Angle = [0.0,0.0,0.0,0.0,0.0,0.0])
myenv.CalculateWithYaw()
myenv.show()