print('Week 13 Functions Project by Innocent Hove. \nEnjoyed this course so much!')
print()
# Defining the function for computing windchill
def wind_chill(value, speed):
    chill = 35.74 + 0.6215 * value - 35.75 * (speed ** 0.16) + 0.4275 * value * (speed ** 0.16)
    return chill
    # Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

# Defining function for converting degrees celcius to degree fahrenheit
def degrees_unit(value):
    return value * (9 / 5) + 32

# Create an empty list and then append the multiples of 5 from 5 to 60
velocity_list = []
for i in range(5, 61, 5):
    velocity_list.append(i)
    
# Name the variable to use in the function and the code
temperature = float(input('What is the temperature? '))
unit = input('Is it degrees Fahrenheit or degrees Celcius (F/C)? ')
degree_symbol = u"\N{DEGREE SIGN}"

# Iterate through each item in the velocity list (i.e. from 5 mph to 60 mph).
print()
for i in velocity_list:
    chill = float((wind_chill(temperature, i)))
    if unit.lower() == 'c':
        # If temperature is degree celcius, convert temperature to degree fahrenheit first by calling the function for degree conversion
        temperature1 = degrees_unit(temperature)
        # temperature1 = temperature * (9 / 5) + 32 # This could be used instead of a function, for similar use

        # Then call the function to compute windchill using the converted temperature.
        chill1 = float((wind_chill(temperature1, i)))
        
        # Print the correct variables
        print(f'At a temperature of {temperature1} {degree_symbol}F, and wind speed of {i} mph, the windchill is {chill1:.2f} {degree_symbol}F.')
    elif unit.lower() == 'f':
        # If fahrenheit then proceed without conversion of temperature unit (no need to call the degrees_unit function)
        print(f'At a temperature of {temperature} {degree_symbol}F, and wind speed of {i} mph, the windchill is {chill:.2f} {degree_symbol}F.')
print()