from floris.tools import FlorisInterface
import numpy as np
# 1. Load an input file
fi = FlorisInterface("inputs/gch.yaml")

# fi.floris.solver

# 2. Modify the inputs with a more complex wind turbine layout
D = 126.0  # Design the layout based on turbine diameter
x = [0, 0,  6 * D, 6 * D]
y = [0, 3 * D, 0, 3 * D]
wind_directions = [270.0, 280.0]
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
yaw_angles = np.zeros( (2, 1, 4) )  # Construct the yaw array with dimensions for two wind directions, one wind speed, and four turbines
yaw_angles[0, :, 0] = 25            # At 270 degrees, yaw the first turbine 25 degrees
yaw_angles[0, :, 1] = 25            # At 270 degrees, yaw the second turbine 25 degrees
yaw_angles[1, :, 0] = 10           # At 265 degrees, yaw the first turbine -25 degrees
yaw_angles[1, :, 1] = 10           # At 265 degrees, yaw the second turbine -25 degrees

# 6. Calculate the velocities at each turbine for all atmospheric conditions with the new yaw settings
fi.calculate_wake(yaw_angles=yaw_angles)

# 7. Get the total farm power
turbine_powers = fi.get_turbine_powers() / 1000.0
farm_power_yaw = np.sum(turbine_powers, 2)

# 8. Compare farm power with and without wake steering
difference = 100 * (farm_power_yaw - farm_power_baseline) / farm_power_baseline
print("Power % difference with yaw")
print(f"    270 degrees: {difference[0, 0]:4.2f}%")
print(f"    280 degrees: {difference[1, 0]:4.2f}%")