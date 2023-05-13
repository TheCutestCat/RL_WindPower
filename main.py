import numpy as np
import matplotlib.pyplot as plt

from floris.tools import FlorisInterface

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

print("Dimensions of `powers`")
print( np.shape(powers) )

N_TURBINES = fi.floris.farm.n_turbines

print()
print("Turbine powers for 8 m/s")
for i in range(2):
    print(f"Wind direction {i}")
    for j in range(N_TURBINES):
        print(f"  Turbine {j} - {powers[i, 0, j]:7,.2f} kW")
    print()

print("Turbine powers for all turbines at all wind conditions")
print(powers)