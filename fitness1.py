# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender: ')
    birth = input('Please enter your birthdate (YYYY-MM-DD): ')
    inch = float(input('Please enter your height in inches: '))
    stone = float(input('Please enter your weight in British Stones: '))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    years = compute_age(birth)
    weight_in_kg = kg_from_lb(stone)
    height_in_cm = cm_from_in(inch)
    bmi = body_mass_index(weight_in_kg, height_in_cm)
    bmr = basal_metabolic_rate(gender, weight_in_kg, height_in_cm, years)
    # Print the results for the user to see.
    print(f'Your age is {years} years old.')
    print(f'Your wight is {weight_in_kg} kgs.')
    print(f'Your BMI is {bmi}.')
    print(f'Your BMR is {bmr} kcal/day.')
    
    pass


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(stone):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    weight_in_kg = stone * 6.35029
    return weight_in_kg
    


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    height_in_cm = inch * 2.54
    return height_in_cm
    


def body_mass_index(weight_in_kg, height_in_cm):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight_in_kg) / height_in_cm**2
    return bmi
    


def basal_metabolic_rate(gender, weight_in_kg, height_in_cm, years):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.lower() == 'male':
        bmr = 88.362 + 13.397 * weight_in_kg + 4.799 * height_in_cm - 5.677 * int(years)
    else:
        bmr = 447.593 + 9.247 * weight_in_kg + 3.098 * height_in_cm - 4.330 * int(years)
    return bmr
        



# Call the main function so that
# this program will start executing.
main()
