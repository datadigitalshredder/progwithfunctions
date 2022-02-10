print('World life expectancies - Spanish Flu.')
print()
from csv import reader
# Approach  -- Without removing the file header!
# Question 1 & 2: Year and country with minimun and maximum expectencies, and the average and standard deviation.

# Variables and list for the entire dataset
expectancy_list = []
country_name = None
country_name1 = None
year_number = -1
expectancy = -1
expectancy1 = 99999999999999999999
expectancy_list_total = 0

# Variables and list for the user year
user_year = int(input('Please enter a year to analyze: '))
expectancy_list1 = []
year_number1 = -1
expectancy2 = -1
expectancy3 = 99999999999999999999
country_name2 = None
country_name3 = None
expectancy_list_total1 = 0

# Variables and list for the user country
user_country = input('Please enter a country/region to analyze: ').title()
expectancy_list2 = []
year_number2 = -1
year_number3 = 999999999999999
expectancy4 = -1
expectancy5 = 9999999999999999
expectancy_list_total2 = 0

# Variables for max drop and max increase
expectancy_list3 = []
expectancy6 = -1
expectancy7 = 99999999999999
expectancy_increase = 0
expectancy_drop = 0
expectancy_difference = 0
final_year_index = 2019
with open('life-expectancy.csv') as expectancies:
    # Skip the header
    expectancies1 = reader(expectancies)
    header = next(expectancies1)
    if header != None:
        for data in expectancies:
            # print(data)
            data1 = data.strip()
            # print(data1)
            data2 = data1.split(',')
            # print(data2)
            country = data2[0]
            country_code = data2[1]
            year = int(data2[2])
            numbers = float(data2[3])
            # print(f'Country: {country} Country code: {country_code} -- Year: {year}, Expectaancy: {numbers}')
        # for i in expectancy_list:
            if numbers != 0:
                expectancy_list.append(numbers)
                if numbers > expectancy:
                    expectancy = numbers
                    country_name = country
                    year_number = year
                if numbers < expectancy1:
                    expectancy1 = numbers
                    country_name1 = country
                    year_number1 = year
        # print(expectancy)
        # print(country_name)
        # print(year_number)
        
        

            
            if user_year == year:
                # year_list.append(user_year)
                expectancy_list1.append(numbers)
                if numbers > expectancy2:
                    expectancy2 = numbers
                    country_name2 = country
                    year_number2 = year
                if numbers < expectancy3:
                    expectancy3 = numbers
                    country_name3 = country
                    year_number3 = year

            if user_country == country.title():
                # year_list.append(user_year)
                expectancy_list2.append(numbers)
                if numbers > expectancy4:
                    expectancy4 = numbers
                    # country_name2 = country
                    year_number4 = year
                if numbers < expectancy5:
                    expectancy5 = numbers
                    # country_name3 = country
                    year_number5 = year
            # if year >= 0:
            #     final_year_indexes = year.index(final_year_index)
            
           
            for l in range(len(expectancy_list) - 1):
                if country == country:
                    expectancy_difference = [expectancy_list[l] - expectancy_list[l + 1]]
                
                    # print(expectancy_difference)
                if numbers > expectancy6:
                    expectancy6 = numbers
                    country_name = country
                    year_number = year
                if numbers < expectancy7:
                    expectancy7 = numbers
                    country_name1 = country
                    year_number1 = year

        # expectancy_difference = [expectancy_list[l] - expectancy_list[l + 1] for l in range(len(expectancy_list) - 1) if country[l] == country[l + 1]]
        # for l in range(len(expectancy_list) - 1):
        #     expectancy_difference = [expectancy_list[l] - expectancy_list[l + 1]]
            # print(expectancy_difference)
                # for l in range(len(expectancy_list) - 1):
                #         expectancy_increase = [expectancy_list[l] - expectancy_list[l + 1]]
                        # expectancy_drop = [expectancy_list[l] - expectancy_list[l + 1]]
                
                # expectancy_drop = [expectancy_list[l] - expectancy_list[l + 1]]

        for i in expectancy_list:
            expectancy_list_total += i
        expectancy_list_average = expectancy_list_total / len(expectancy_list)

    # print(expectancy_list)
    # print(expectancy_list1)
    # print(len(expectancy_list1))

    

        for j in expectancy_list1:
            expectancy_list_total1 += j
        expectancy_list_average1 = expectancy_list_total1 / len(expectancy_list1)

        for k in expectancy_list2:
            expectancy_list_total2 += k
        expectancy_list_average2 = expectancy_list_total2 / len(expectancy_list2)

        
        # expectancy_list3.append(expectancy_difference)
        print()
        print(f'For the entire dataset: \n The average life expectancy is {expectancy_list_average:.2f} years.')
        print(f' The lowest life expectancy was {expectancy1} years from {country_name1} in {year_number1}.')
        print(f' The highest life expectancy was {expectancy} years from {country_name} in {year_number}')   
        print()   
        print(f'For the year {user_year}: \n The average life expectancy is {expectancy_list_average1:.2f} years. \n The lowest life expectancy was {expectancy3} years from {country_name3}. \n The highest life expectancy was {expectancy2} years from {country_name2}.')
        print()
        print(f'For the country/region {user_country}: \n The average life expectancy is {expectancy_list_average2:.2f} years. \n The lowest life expectancy was {expectancy5} years in {year_number5}. \n The highest life expectancy was {expectancy4} years in {year_number4}.')
        print(expectancy_difference)
        # print(expectancy_drop)
        # print(expectancy_list3)
        
        
    # print(expectancy_list_total)
    # print(expectancy_list_average)
#                 # OR USE:
#             # if country != '':
#                 country_list.append(country)
#             if year != 0:
#                 year_list.append(year)
#             if numbers != 0:
#                 expectancy_list.append(numbers)
#     # print(expectancy_list)
#     # print(country_list)
#     # print(year_list)
#     biggest_expectancy = max(expectancy_list)
#     biggest_expectancy_index = expectancy_list.index(biggest_expectancy)
#     # print(f'The biggest life expectancy is: {biggest_expectancy}.')
#     smallest_expectancy = min(expectancy_list)
#     smallest_expectancy_index = expectancy_list.index(smallest_expectancy)
#     average = sum(expectancy_list) / len(expectancy_list)
#     standard_dev = statistics.stdev(expectancy_list)
#     # print(smallest_expectancy_index)
#     # print(f'The smallest life expectancy is: {smallest_expectancy}.')
#     print()
#     print(f'For this data set: \nThe overall maximum life expectancy is {biggest_expectancy:.2f} years from {country_list[biggest_expectancy_index]} in {year_list[biggest_expectancy_index]}.')
#     print(f'The overall minimum life expectancy is {smallest_expectancy:.2f} years from {country_list[smallest_expectancy_index]} in {year_list[smallest_expectancy_index]}.')
#     print(f'The average life expectancy is {average:.2f} years with a standard deviation of {standard_dev:.2f} years.')
#     print()

# # Question 3: Average, minimum, and maximum expectancies for a given user year and user Country.

# country_list = []
# year_list = []
# all_country_list = []
# expectancy_list = []

# user_year = int(input('Please enter a year to analyze: '))
# user_country = input('Please enter a country/region to analyze: ').title()
# comparison_country = input('Please enter a country/region to compare with: ').title()

# with open('life-expectancy.csv') as expectancies:
#     expectancies1 = reader(expectancies)
#     header = next(expectancies1)
    
#     if header != None:
#     # import csv
#     # expectancies1 = csv.reader(expectancies)
#     # next(expectancies1)
#         for data in expectancies:
#             # print(data)
#             data2 = data.strip().split(',')
#             # print(data1)
#             # data2 = data1.split(',')
#             # print(data2)
#             country = data2[0]
#             country_code = data2[1]
#             year = int(data2[2])
#             numbers = float(data2[3])
            
#             if year != 0:
#                 year_list.append(year)
#                 # user_year_country_list.append(country)
#             if country != None:
#                 # OR USE:
#             # if country != '':
#                 country_list.append(country)
#             if numbers != 0:
#                 expectancy_list.append(numbers)
#             if numbers != 0:
                
#                 indices = [i for i, v in enumerate(year_list) if v == user_year]              
#                 indices1 = [i for i, v in enumerate(country_list) if v == user_country]
#                 indices2 = [j for j, w in enumerate(country_list) if w == comparison_country]
#                 indices3 = [k for k, x in enumerate(year_list) if x == user_year]

#                 indices_to_access = indices
#                 indices_to_access1 = indices1
#                 indices_to_access2 = indices2
#                 indices_to_access3 = indices3

#                 accessed_mapping = map(expectancy_list.__getitem__, indices_to_access)
#                 accessed_list = list(accessed_mapping)
#                 # Making it my own 1
#                 accessed_mapping1 = map(country_list.__getitem__, indices_to_access1)
#                 accessed_list1 = list(accessed_mapping1)

#                 accessed_mapping2 = map(expectancy_list.__getitem__, indices_to_access1)
#                 accessed_list2 = list(accessed_mapping2)

#                 # To comparison two countries
#                 accessed_mapping3 = map(expectancy_list.__getitem__, indices_to_access2)
#                 accessed_list3 = list(accessed_mapping3)

#                 accessed_mapping4 = map(expectancy_list.__getitem__, indices_to_access3)
#                 accessed_list4 = list(accessed_mapping4)

#                 # Making it my own 2
#                 expectancy_increase = [expectancy_list[i + 1] - expectancy_list[i] for i in range(len(expectancy_list) - 1)]
#                 expectancy_drop = [expectancy_list[i] - expectancy_list[i + 1] for i in range(len(expectancy_list) - 1)]
#                 expectancy_drop1 = [expectancy_list[i] - expectancy_list[i + 1] for i in range(len(expectancy_list) - 1)]
#                 # expectancy_drop2 = [expectancy_list[i + 1] - expectancy_list[i] for i in range(len(expectancy_list) - 1)]
                    
#     user_total = sum(accessed_list)
#     user_country_total = sum(accessed_list2)
#     comparison_total = sum(accessed_list3)

#     user_year_items_len = len(accessed_list)
#     user_country_item_len = len(accessed_list2)
#     comparison_item_len = len(accessed_list3)

#     year_average = user_total / user_year_items_len
#     country_average = user_country_total / user_country_item_len
#     comparison_average = comparison_total / comparison_item_len

#     max_expectancy = max(accessed_list2)
#     max_expectancy_index = accessed_list2.index(max_expectancy)

#     min_expectancy = min(accessed_list2)
#     min_expectancy_index = accessed_list2.index(min_expectancy)

#     max_year_expectancy = max(accessed_list4)
#     max_year_expectancy_index = accessed_list4.index(max_year_expectancy)
#     min_year_expectancy = min(accessed_list4)
#     min_year_expectancy_index = accessed_list4.index(min_year_expectancy)

#     user_country_max_expectency = max(accessed_list2)
#     user_country_min_expectancy = min(accessed_list2)

#     comparison_max_expectancy = max(accessed_list3)
#     comparison_min_expectancy = min(accessed_list3)
     
#     min_drop = min(i for i in expectancy_drop if i > 0)
#     min_drop_index = expectancy_drop.index(min_drop) + 1

#     max_drop = max(i for i in expectancy_drop1 if i < 8.73)
#     max_drop_index = expectancy_drop1.index(max_drop) + 1

#     # OR
#     # max_drop1 = max(expectancy_drop2)
#     # max_drop1_index = expectancy_drop2.index(max_drop1)

#     max_increase = max(expectancy_increase)
#     max_increase_index = expectancy_increase.index(max_increase) + 1

#     country_index = country_list[max_increase_index]
#     year_index = year_list[max_increase_index]

#     country_index1 = country_list[min_drop_index]
#     year_index1 = year_list[min_drop_index]

#     country_index2 = country_list[max_drop_index]
#     year_index2 = year_list[max_drop_index]

#     country_index3 = country_list[min_year_expectancy_index]
#     # year_index3 = year_list[max_drop_index]

#     country_index4 = country_list[max_year_expectancy_index]
#     # year_index4 = year_list[max_drop_index]

#     print()
#     print(f'The maximum drop in life expectancies was {max_drop:.4f} years in {country_index2} in the year {year_index2}.')
#     print()
#     print(f'The minimum drop in life expectancies was {min_drop:.4f} years in {country_index1} in the year {year_index1}.')
#     print()
#     print(f'The largest increase in life expectancies was {max_increase:.4f} years in {country_index} in the year {year_index}.')
#     print()
#     # print(f'For the year: {user_year}, \n The average expectancy is {year_average:.4f} years. \n The minimum expectancy was {min_year_expectancy:.4f} years in {accessed_list[min_year_expectancy]}. \n The maximum expectancy was {max_year_expectancy:.4f} years in year {accessed_list[max_year_expectancy]}.')
#     print(f'For the year: {user_year}, \n The average expectancy is {year_average:.4f} years. \n The minimum expectancy was {min_year_expectancy:.4f} years in {country_list[smallest_expectancy_index]}. \n The maximum expectancy was {max_year_expectancy:.4f} years {country_list[biggest_expectancy_index]}.')
#     print()
#     print(f'For country/region: {user_country}, \n The average expectancy is {country_average:.4f} years. \n The minimun expectancy was {user_country_min_expectancy:.4f} years. \n The maximum expectancy was {user_country_max_expectency:.4f} years.')
#     print()

#     # print(comparison_total)
#     # print(comparison_item_len)
#     print('Here is the comparison for your selected countries/regions:')
#     print(f'For {user_country}: \n The average expectancy is {country_average:.4f} years. \n The minimun expectancy was {user_country_min_expectancy:.4f} years. \n The maximum expectancy was {user_country_max_expectency:.4f} years. \n...')
#     print(f'WHILE for {comparison_country}: \n The average expectancy is {comparison_average:.4f} years. \n The minimun expectancy was {comparison_max_expectancy:.4f} years. \n The maximum expectancy was {comparison_min_expectancy:.4f} years.')
#     print()