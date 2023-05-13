import numpy as np
import matplotlib.pyplot as plt

from floris.tools import FlorisInterface
from floris.tools.visualization import visualize_cut_plane

fi = FlorisInterface("inputs/gch.yaml")

x_2x2 = [0, 0, 800, 800]
y_2x2 = [0, 400, 0, 400]
yaw_angles = np.zeros((2, 2, 4))
print("Yaw angle array initialized with 0's")
print(yaw_angles)

print("First turbine yawed 25 degrees for every atmospheric condition")
yaw_angles[:, :, 0] = 25
print(yaw_angles)

fi.reinitialize(layout_x=x_2x2, layout_y=y_2x2)

fi.reinitialize(wind_directions=[270.0, 280.0], wind_speeds=[8.0,9.0])

fi.calculate_wake(yaw_angles=yaw_angles)

powers = fi.get_turbine_powers() / 1000.0  # calculated in Watts, so convert to kW

N_TURBINES = fi.floris.farm.n_turbines

fig, axarr = plt.subplots(2, 2, figsize=(15,8))
wind_directions=[270.0, 280.0]
horizontal_plane = fi.calculate_horizontal_plane(height=90.0)
visualize_cut_plane(horizontal_plane, ax=axarr[0,0], title="270 - Aligned")

# horizontal_plane = fi.calculate_horizontal_plane(wd=[wind_directions[0]], yaw_angles=yaw_angles[0:1,0:1] , height=90.0)
# visualize_cut_plane(horizontal_plane, ax=axarr[0,1], title="270 - Yawed")
#
# horizontal_plane = fi.calculate_horizontal_plane(wd=[wind_directions[1]], height=90.0)
# visualize_cut_plane(horizontal_plane, ax=axarr[1,0], title="280 - Aligned")
#
# horizontal_plane = fi.calculate_horizontal_plane(wd=[wind_directions[1]], yaw_angles=yaw_angles[1:2,0:1] , height=90.0)
# visualize_cut_plane(horizontal_plane, ax=axarr[1,1], title="280 - Yawed")

plt.show()