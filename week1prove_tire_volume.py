
# Print what this progaram does
print('Tire sizes in the US')

# Import the math module
import math
print()

# Request variables from the user
tire_width = float(input('What is the tire width in millimeters? '))
aspect_ratio = float(input('What is the aspect ratio of the tire? '))
wheel_diameter = float(input('What is the wheel diameter in inches? '))

# Compute the volume in parts
tire_volume = math.pi * (tire_width ** 2) * aspect_ratio
ratio = tire_width * aspect_ratio
diameter = 2540 * wheel_diameter

volume_inside_tire = (tire_volume * (ratio + diameter)) / 10000000000

# OR compute the volume at once
volume_inside_tire = (math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000

# Display volume
print(f'The volume of space inside wheel is: \n {volume_inside_tire:.2f} liters.')
print()
