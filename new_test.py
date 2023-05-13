from floris.tools import FlorisInterface
import numpy as np
from matplotlib import pyplot as plt

# 1. Load an input file
fi = FlorisInterface("inputs/gch.yaml")

# fi.floris.solver

# 2. Modify the inputs with a more complex wind turbine layout
D = 126.0  # Design the layout based on turbine diameter

x = [0, 0,  6 * D, 6 * D, 12*D,12*D]
y = [0, 3 * D, 0, 3 * D,0,3*D]
wind_directions = [270.0]
wind_speeds = [8.0]

# Pass the new data to FlorisInterface
fi.reinitialize(
    layout_x=x,
    layout_y=y,
    wind_directions=wind_directions,
    wind_speeds=wind_speeds
)

# 3. Calculate the velocities at each turbine for all atmospheric conditions
# All turbines have 0 degrees yaw
fi.calculate_wake()

# 4. Get the total farm power
turbine_powers = fi.get_turbine_powers() / 1000.0  # Given in W, so convert to kW
farm_power_baseline = np.sum(turbine_powers, 2)  # Sum over the third dimension

# 5. Develop the yaw control settings
yaw_angles = np.zeros( (1, 1, 6) )  # Construct the yaw array with dimensions for two wind directions, one wind speed, and four turbines
yaw_angles[0, :, 0] = 30            # At 270 degrees, yaw the first turbine 25 degrees
yaw_angles[0, :, 1] = 0          # At 270 degrees, yaw the second turbine 25 degrees
yaw_angles[0, :, 2] = 0            # At 270 degrees, yaw the first turbine 25 degrees
yaw_angles[0, :, 3] = 0          # At 270 degrees, yaw the second turbine 25 degrees
yaw_angles[0, :, 4] = 0            # At 270 degrees, yaw the first turbine 25 degrees
yaw_angles[0, :, 5] = 0          # At 270 degrees, yaw the second turbine 25 degrees

# 6. Calculate the velocities at each turbine for all atmospheric conditions with the new yaw settings
# fi.calculate_wake(yaw_angles=yaw_angles)
#
# # 7. Get the total farm power
# turbine_powers = fi.get_turbine_powers() / 1000.0
# farm_power_yaw = np.sum(turbine_powers, 2)
#
# # 8. Compare farm power with and without wake steering
# difference = 100 * (farm_power_yaw - farm_power_baseline) / farm_power_baseline
# print("Power % difference with yaw")
# print(f"    270 degrees: {difference[0, 0]:4.2f}%")
#
# from floris.tools.visualization import visualize_cut_plane
#
# fig, axarr = plt.subplots(2, 1, figsize=(15,8))
#
# horizontal_plane = fi.calculate_horizontal_plane(wd=[wind_directions[0]], height=90.0)
# visualize_cut_plane(horizontal_plane, ax=axarr[0], title="270 - Aligned")
#
# horizontal_plane = fi.calculate_horizontal_plane(wd=[wind_directions[0]], yaw_angles=yaw_angles[0:1,0:1] , height=90.0)
# visualize_cut_plane(horizontal_plane, ax=axarr[1], title="270 - Yawed")
#
# plt.show()