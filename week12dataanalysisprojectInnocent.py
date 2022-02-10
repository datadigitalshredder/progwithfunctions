print('World life expectancies - Spanish Flu.')

import statistics

import numpy as np
# import matplotlib.pyplot as plt
from csv import reader
# Approach 1 -- removing the header in the .csv file before iterating
# expectancy_list = []
# with open('life-expectancy1.csv') as expectancies:
#     for data in expectancies:
#         # print(data)
#         data1 = data.strip()
#         # print(data1)
#         data2 = data1.split(',')
#         # print(data2)
#         country = data2[0]
#         country_code = data2[1]
#         year = data2[2]
#         numbers = float(data2[3])
#         # print(f'Country: {country} Country code: {country_code} -- Year: {year}, Expectaancy: {numbers}')
#         if numbers != 0:
#             expectancy_list.append(numbers)
# # print(expectancy_list)
# biggest_expectancy = max(expectancy_list)
# print(f'The biggest life expectancy is: {biggest_expectancy}.')
# smallest_expectancy = min(expectancy_list)
# print(f'The smallest life expectancy is: {smallest_expectancy}.')

# Approach 2 -- Without removing the file header!
# Question 1 & 2: Year and country with minimun and maximum expectencies, and the average and standard deviation.

# Create these lists to add different items of the split .csv file
country_list = []
year_list = []
expectancy_list = []

with open('life-expectancy.csv') as expectancies:
    # Skip the header row of the .csv file
    expectancies1 = reader(expectancies)
    header = next(expectancies1)
    if header != None:
        # Start iterating
        for data in expectancies:
            data1 = data.strip()
            data2 = data1.split(',')
            country = data2[0]
            country_code = data2[1]
            year = int(data2[2])
            numbers = float(data2[3])
            if country != None:
                # OR USE:
            # if country != '':
                country_list.append(country)
            if year != 0:
                year_list.append(year)
            if numbers != 0:
                expectancy_list.append(numbers)

    # After the for loop, set variables for the different parameters from the data
    biggest_expectancy = max(expectancy_list)
    biggest_expectancy_index = expectancy_list.index(biggest_expectancy)

    smallest_expectancy = min(expectancy_list)
    smallest_expectancy_index = expectancy_list.index(smallest_expectancy)

    average = sum(expectancy_list) / len(expectancy_list)
    standard_dev = statistics.stdev(expectancy_list)
    
    # Compute the correlation (relationship) between the increase in years and the increase in life expectancy and set the boolean variable for it.
    correlation_coefficient = np.corrcoef(year_list, expectancy_list)
    if correlation_coefficient[0,1] >= 0.5:
        relationship = True
    else:
        relationship = False

    print()
    print(f'For the entire dataset: \nThe maximum life expectancy is {biggest_expectancy:.2f} years from {country_list[biggest_expectancy_index]} in {year_list[biggest_expectancy_index]}.')
    print(f' The minimum life expectancy is {smallest_expectancy:.2f} years from {country_list[smallest_expectancy_index]} in {year_list[smallest_expectancy_index]}.')
    print(f' The average life expectancy is {average:.2f} years with a standard deviation of {standard_dev:.2f} years.')
    print(f' The correlation coefficient between the increase in years and increase in life expectancy is {correlation_coefficient[0,1]:.2f}.')
    if relationship:
        print(' This is a moderate to strong positive linear relationship between increase in years and increase in life expectancies.')
    else:
        print(' This is a weak to negative correlation between increase years and increase life expectancies.')
    print()

# Question 3: Average, minimum, and maximum expectancies for a given user year and user country.

country_list = []
year_list = []
expectancy_list = []

# expectancy list for list without the 2019 expectancy
expectancy_list1 = []
year_list1 = []
country_list1 = []

# Request input information from the user
user_year = int(input('Please enter a year to analyze: '))
user_country = input('Please enter a country/region to analyze: ').title()
comparison_country = input('Please enter a country/region to compare with: ').title()

# Open the .csv file again
with open('life-expectancy.csv') as expectancies:
    expectancies1 = reader(expectancies)
    header = next(expectancies1)
    
    if header != None:
        for data in expectancies:
            data1 = data.strip().split(',')
            country = data1[0]
            country_code = data1[1]
            year = int(data1[2])
            numbers = float(data1[3])
            
            if year != 0:
                year_list.append(year)
                year_list1.append(year)
            if country != None:
                # OR USE:
            # if country != '':
                country_list.append(country)
                country_list1.append(country)
            if numbers != 0:
                expectancy_list.append(numbers)
                expectancy_list1.append(numbers)

    # Set new variables to access the indices of the user year, user country, and user comparison country from the main .csv file using the enumerate function
    indices = [i for i, v in enumerate(year_list) if v == user_year]              
    indices1 = [i for i, v in enumerate(country_list) if v == user_country]
    indices2 = [j for j, w in enumerate(country_list) if w == comparison_country]
    # The index of year 2019 in main year list to use later when removing the expectancy drop at year 2019 to the next year
    indices3 = [k for k, x in enumerate(year_list) if x == 2019]

    # After setting the indices into list, access the values of those indices are from the lists created, i.e. country_list, year_list etc.
    # The goal is to access using the above indices what the user year, user country, user comparison country and the corresponding expectencies.

    # 1. Accessing the expectencies using the user year
    accessed_mapping = map(expectancy_list.__getitem__, indices)
    accessed_list = list(accessed_mapping)
    # 2. Accessing the country using the user country
    accessed_mapping1 = map(country_list.__getitem__, indices1)
    accessed_list1 = list(accessed_mapping1)
    # 3. Accessing the expectencies and years using the user country and comparison country
    accessed_mapping2 = map(expectancy_list.__getitem__, indices1)
    accessed_list2 = list(accessed_mapping2)

    accessed_mapping4 = map(year_list.__getitem__, indices1)
    accessed_list4 = list(accessed_mapping4)

    accessed_mapping5 = map(year_list.__getitem__, indices2)
    accessed_list5 = list(accessed_mapping5)

    # accessed_mapping6 = map(year_list.__getitem__, indices3)
    # accessed_list6 = list(accessed_mapping6)

    # To compare two countries
    # 4. Accessing the expectencies using the user comparison country
    accessed_mapping3 = map(expectancy_list.__getitem__, indices2)
    accessed_list3 = list(accessed_mapping3)

    # Compute the expectency total for user year, user country, and user comparison country respectively              
    user_total = sum(accessed_list)
    user_country_total = sum(accessed_list2)
    comparison_total = sum(accessed_list3)

    # Determine the len of the lists 
    user_year_items_len = len(accessed_list)
    user_country_item_len = len(accessed_list2)
    comparison_item_len = len(accessed_list3)

    # Compute the average
    year_average = user_total / user_year_items_len
    country_average = user_country_total / user_country_item_len
    comparison_average = comparison_total / comparison_item_len

    # Determine the max and min expectencies of all the data and their indices
    max_expectancy = max(accessed_list2)
    max_expectancy_index = accessed_list2.index(max_expectancy)
    min_expectancy = min(accessed_list2)
    min_expectancy_index = accessed_list2.index(min_expectancy)

    # Determine the max and min expectencies of the user year and their indices
    max_year_expectancy = max(accessed_list)
    max_year_expectancy_index = expectancy_list.index(max_year_expectancy)
    min_year_expectancy = min(accessed_list)
    min_year_expectancy_index = expectancy_list.index(min_year_expectancy)

    # Determine the max and min user country and their indices
    user_country_max_expectancy = max(accessed_list2)
    user_country_max_expectancy_index = accessed_list2.index(user_country_max_expectancy)
    user_country_min_expectancy = min(accessed_list2)
    user_country_min_expectancy_index = accessed_list2.index(user_country_min_expectancy)

    # Determine the max and min comparison country and indices
    comparison_max_expectancy = max(accessed_list3)
    comparison_max_expectancy_index = accessed_list3.index(comparison_max_expectancy)
    comparison_min_expectancy = min(accessed_list3)
    comparison_min_expectancy_index = accessed_list3.index(comparison_min_expectancy)

    # Determining the increase and drop in expectencies from one year to the next
    # The drop is detemined by subtracting one year to the next year, while the increase is the reverse from the second year to the previous.
    expectancy_increase = [expectancy_list[i + 1] - expectancy_list[i] for i in range(len(expectancy_list) - 1)]
    
    # When iterating for max drop expectencies from one year to the next, the max drop will be the drop between the last year of one country 
    # to the first year of the next country. We want the country with the max drop.
    # Note that the maximum drop from one to the next is between  year 2019 of one country to first year of the next country. This is misleading, we want the max drop with one country.
    expectancy_drop = [expectancy_list[i] - expectancy_list[i + 1] for i in range(len(expectancy_list) - 1)]
    expectancy_drop1 = [expectancy_list[i] - expectancy_list[i + 1] for i in range(len(expectancy_list) - 1)]

    # Removing the item at year 2019 index in the concurrent expectancy, year, and country lists so that the max drop in life expectancies is within not between countries.
    removed = [expectancy_drop1[i] for i in range(len(expectancy_drop1)) if i not in indices3]
    for i in sorted(indices3, reverse = True):
        expectancy_drop1.pop(i - 1)

    removed1 = [country_list1[i] for i in range(len(country_list1)) if i not in indices3]
    for i in sorted(indices3, reverse = True):
        country_list1.pop(i - 1)
    
    removed2 = [year_list1[i] for i in range(len(year_list1)) if i not in indices3]
    for i in sorted(indices3, reverse = True):
        year_list1.pop(i - 1)
    # expectancy_drop2 = [expectancy_list[i + 1] - expectancy_list[i] for i in range(len(expectancy_list) - 1)]

    # Determine the max and min drop expectancies
    min_drop = min(j for j in expectancy_drop if j > 0)
    min_drop_index = expectancy_drop.index(min_drop) + 1
    max_drop = max(removed)
    max_drop_index = removed.index(max_drop) + 1

    # Determine the max increase
    max_increase = max(expectancy_increase)
    max_increase_index = expectancy_increase.index(max_increase) + 1

    # These are the indices for the max and min drops and increases
    country_index = country_list[max_increase_index]
    year_index = year_list[max_increase_index]

    country_index1 = country_list[min_drop_index]
    year_index1 = year_list[min_drop_index]

    # Determining the country and year with max drop expectancy after removing the year and country with year 2019
    country_index2 = country_list1[max_drop_index]
    year_index2 = year_list1[max_drop_index]

    # These are the country indices for min and max expectancy of the user year 
    country_index3 = country_list[min_year_expectancy_index]
    country_index4 = country_list[max_year_expectancy_index]

    print()
    print(f'For the entire dataset: \nThe maximum drop in life expectancies was {max_drop:.3f} years in {country_index2} in the year {year_index2}.')
    print(f'The minimum drop in life expectancies was {min_drop:.3f} years in {country_index1} in the year {year_index1}.')
    print(f'The largest increase in life expectancies was {max_increase:.2f} years in {country_index} in the year {year_index}.')
    print()
    print(f'For the year: {user_year}, \n The average life expectancy is {year_average:.2f} years. \n The minimum expectancy was {min_year_expectancy:.3f} years in {country_index3}. \n The maximum expectancy was {max_year_expectancy:.3f} years in {country_index4}.')
    # print(f'For the year: {user_year}, \n The average expectancy is {year_average:.4f} years. \n The minimum expectancy was {min_year_expectancy:.4f} years in {country_list[min_year_expectancy_index]}. \n The maximum expectancy was {max_year_expectancy:.4f} years in {country_list[max_year_expectancy_index]}.')

    # print()
    # print(f'For country/region: {user_country}, \n The average expectancy is {country_average:.4f} years. \n The minimun expectancy was {user_country_min_expectancy:.4f} years in {accessed_list4[user_country_min_expectancy_index]}. \n The maximum expectancy was {user_country_max_expectancy:.4f} years in {accessed_list4[user_country_max_expectancy_index]}.')
    print()

    print('Here is a comparison of your selected countries/regions:')
    # print(f'For {user_country}: \n The average expectancy is {country_average:.4f} years. \n The minimun expectancy was {user_country_min_expectancy:.4f} years. \n The maximum expectancy was {user_country_max_expectancy:.4f} years. \n...')
    print(f'For {user_country}: \n The average life expectancy is {country_average:.2f} years. \n The minimun expectancy was {user_country_min_expectancy:.3f} years in {accessed_list4[user_country_min_expectancy_index]}. \n The maximum expectancy was {user_country_max_expectancy:.3f} years in {accessed_list4[user_country_max_expectancy_index]}. \n...')
    print(f'WHILE for {comparison_country}: \n The average life expectancy is {comparison_average:.2f} years. \n The minimun expectancy was {comparison_min_expectancy:.3f} years in {accessed_list5[comparison_min_expectancy_index]}. \n The maximum expectancy was {comparison_max_expectancy:.3f} years in {accessed_list5[comparison_max_expectancy_index]}.')
    print()
