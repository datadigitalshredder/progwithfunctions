# family_history.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2

# In order to count the number of marriages for each one way is to create the marriage list and make it global.
marriage_list = []
marriage_list_names = []

import collections
def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # print(f'The number of males is {male}. \nThe number of females is {female}.')

    # Print a blank line.
    print()

    # Call the count_marriges function to count
    # and print the number of marriages.
    count_marriages(marriages_dict)
    # print(marriage_list)

    for _ in marriage_list:
        details = people_dict[_] # Get the value for each key in the people dictionary 
        name_detail = details[NAME_INDEX] # Extracting the actual name using the name key index
        marriage_list_names.append(name_detail)
        
        occurrences = collections.Counter(marriage_list_names) # Count the number of times, each appears in the marriage, corrresponds to the number of marriages
    print(occurrences)
    
    print()
    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for _ in people_dict:
        person = people_dict[_] # For each key in the dictionary, create the people info list
        person_name = person[NAME_INDEX] # For each person, get their names from the list
        person_age = person[DEATH_YEAR_INDEX] - person[BIRTH_YEAR_INDEX] # For each person, get their age at death
        print(f'Name: {person_name}, Age: {person_age}. Born {person[BIRTH_YEAR_INDEX]} and died {person[DEATH_YEAR_INDEX]}.')


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male = 0
    female = 0

    for i in people_dict:
        gender = people_dict[i]
        gender_type = gender[GENDER_INDEX]
        if gender_type == 'M':
            male += 1
        elif gender_type == 'F':
            female += 1
    
    print(f'The number of males is {male}. \nThe number of females is {female}.')

def count_marriages(marriage_dict):
    """Count and print the number of marriages each person has had.

    Parameter
        marriage_dict: a dictionary that contains data about marriages
            Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
    Return: nothing
    """
    
    print('These are the number of marriages each person had:')
    for i in marriage_dict:
        individual = marriage_dict[i]
        husband_ref = individual[HUSBAND_KEY_INDEX]
        wife_ref = individual[WIFE_KEY_INDEX]
        marriage_list.append(husband_ref)
        marriage_list.append(wife_ref)

def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """

    print('The marriages were:')
    
    # Use nested for loops to iterate in the two dictionaries and extract the people and marriage information

    for j in marriages_dict:
        couple = marriages_dict[j] # Create lists for each key in the marriage dictionary
        husnames = couple[HUSBAND_KEY_INDEX] # For each list, extract the husband reference index using the husband key index and assign it a variable
        wifenames = couple[WIFE_KEY_INDEX] # For each list, extract the wife reference index using the husband key index and assign it a variable
        marriage_year = couple[WEDDING_YEAR_INDEX] # From eanch list extract the marriage year

        for _ in people_dict:
            hus_details = people_dict[husnames] # The husbands lists 
            husband_name = hus_details[NAME_INDEX] # Extracting the actual husband name
            hus_age = marriage_year - hus_details[BIRTH_YEAR_INDEX] # the husband's age

            wife_details = people_dict[wifenames] # The wives lists
            wife_name = wife_details[NAME_INDEX] # Extracting the actual wife name
            wife_age = marriage_year - wife_details[BIRTH_YEAR_INDEX]

        # Print the husband and wife name, their ages, and marriage year
        print(f'{husband_name} aged {hus_age} and {wife_name} aged {wife_age} in {marriage_year}.')

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
