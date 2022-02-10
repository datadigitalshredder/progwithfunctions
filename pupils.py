import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    students_list = read_compound_list('pupils.csv')

    birthdate = lambda date: date[BIRTHDATE_INDEX]

    sorted_birthdate = sorted(students_list, key=birthdate)

    # pupil_list = print_list(sorted_birthdate)

    # for student in pupil_list:
    #     print(student)
    for i in sorted_birthdate:
        print(i)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)
    return compound_list


def print_list(pupils_list):
    """Prints each element of the list on a separate line.
    Parameters:
        Pupils list
    Return value:
        The pupils list"""
    
    for pupil in pupils_list:
        print(pupil)

if __name__ == '__main__':
    main()
    
# import csv


# # Each row in the pupils.csv file contains three elements.
# # These are the indexes of the elements in each row.
# GIVEN_NAME_INDEX = 0
# SURNAME_INDEX = 1
# BIRTHDATE_INDEX = 2
# students_list = []
# def main():
#     try:
#         students_list = read_compound_list("pupils.csv")
#         print(students_list)

#         given_name = students_list[0]
#         surname = students_list[1]
#         birthday = students_list[2]
#         # birth_month_day = birthday[5:]
#         print()

#         birthdays_func = lambda birthday: birthday[BIRTHDATE_INDEX] 
#         sorted_b_list = sorted(students_list, key=birthdays_func)
#         print("Ordered list from Oldest to Youngest")
#         for birthdate in sorted_b_list:
#             print(birthdate)
#         print()


#         given_name_func = lambda given_name: given_name[GIVEN_NAME_INDEX]
#         sorted_gn_name = sorted(students_list, key=given_name_func)
#         print("Ordered list by Given name")
#         for given_name in sorted_gn_name:
#             print(given_name)
#         print()

#         surname_func = lambda surname: surname[SURNAME_INDEX]
#         sorted_surname = sorted(students_list, key=surname_func)
#         print("Ordered list from by Surname")
#         for surname in sorted_surname:
#             print(surname)

#     except (IndexError, FileNotFoundError, PermissionError) as error:
#         print(type(error)._name_, error, sep=": ")

# def read_compound_list(filename):
#         """Read the text from a CSV file into a compound list.
#         The compound list will contain small lists. Each small
#         list will contain the data from one row of the CSV file.

#         Parameter
#             filename: the name of the CSV file to read.
#         Return: the compound list
#         """
#         # Create an empty list.
#         compound_list = []

#         # Open the CSV file for reading.
#         with open(filename, "rt") as csv_file:

#             # Use the csv module to create a reader
#             # object that will read from the opened file.
#             reader = csv.reader(csv_file)

#             # The first line of the CSV file contains column headings
#             # and not a student's I-Number and name, so this statement
#             # skips the first line of the CSV file.
#             next(reader)

#             # Process each row in the CSV file.
#             for row in reader:

#                 # Append the current row at the end of the compound list.
#                 compound_list.append(row)

#         return compound_list

# def print_list(student_list):
#     for pupils in student_list:
#         return pupils



# # Call main to start this program.
# if __name__ == "__main__":
#     main()
   