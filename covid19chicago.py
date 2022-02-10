import numpy as np
import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt




def main():
    covid_data = read_covid19('COVID-19-Daily-tests.csv')

    day_list = []
    pos_test_list = []
    neg_test_list = []
    total_test_list = []
    test_0_17_yrs_list = []
    test_18_29_yrs_list = []
    test_30_39_yrs_list = []
    test_40_49_yrs_list = []
    test_50_59_yrs_list = []
    test_60_69_yrs_list = []
    test_70_79_yrs_list = []
    test_80yrs_list = []
    test_unknown_yrs_list = []
    test_gender_female_list = []
    test_gender_male_list = []
    test_gender_unknown_list = []
    test_race_latinx_list = []
    test_race_asian_list = []
    test_race_black_list = []
    test_race_white_list = []
    test_race_other_race_list = []
    test_race_unknown_list = []
    pos_test_0_17_yrs_list = []
    pos_test_18_29_yrs_list = []
    pos_test_30_39_yrs_list = []
    pos_test_40_49_yrs_list = []
    pos_test_50_59_yrs_list = []
    pos_test_60_69_yrs_list = []
    pos_test_70_79_yrs_list = []
    pos_test_80yrs_list = []
    pos_test_unknown_yrs_list = []
    neg_test_0_17_yrs_list = []
    neg_test_18_29_yrs_list = []
    neg_test_30_39_yrs_list = []
    neg_test_40_49_yrs_list = []
    neg_test_50_59_yrs_list = []
    neg_test_60_69_yrs_list = []
    neg_test_70_79_yrs_list = []
    neg_test_80yrs_list = []
    neg_test_unknown_yrs_list = []
    pos_test_female_list = []
    pos_test_male_list = []
    pos_test_unk_gender_list = []
    neg_test_female_list = []
    neg_test_male_list = []
    neg_test_unk_gender_list = []
    pos_test_latinx_list = []
    pos_test_asian_list = []
    pos_test_black_list = []
    pos_test_white_list = []
    pos_test_other_race_list = []
    pos_test_race_unknown_list = []
    neg_test_latinx_list = []
    neg_test_asian_list = []
    neg_test_black_list = []
    neg_test_white_list = []
    neg_test_other_race_list = []
    neg_test_race_unknown_list = []

    for i in covid_data:
        data = covid_data[i]
        # print(i, data)
        day = data[0]
        day_list.append(day)
        pos_test = data[1]
        pos_test_list.append(pos_test)
        neg_test = data[2]
        neg_test_list.append(neg_test)
        total_test = data[3]
        total_test_list.append(total_test)

        test_0_17_yrs = data[4]
        test_0_17_yrs_list.append(test_0_17_yrs)
        test_18_29_yrs = data[5]
        test_18_29_yrs_list.append (test_18_29_yrs)
        test_30_39_yrs = data[6]
        test_30_39_yrs_list.append(test_30_39_yrs)
        test_40_49_yrs = data[7]
        test_40_49_yrs_list.append(test_40_49_yrs)
        test_50_59_yrs = data[8]
        test_50_59_yrs_list.append(test_50_59_yrs)
        test_60_69_yrs = data[9]
        test_60_69_yrs_list.append(test_60_69_yrs)
        test_70_79_yrs = data[10]
        test_70_79_yrs_list.append(test_70_79_yrs)
        test_80yrs = data[11]
        test_80yrs_list.append(test_80yrs)
        test_unknown_yrs = data[12]
        test_unknown_yrs_list.append(test_unknown_yrs)

        test_gender_female = data[13]
        test_gender_female_list.append(test_gender_female)
        test_gender_male = data[14]
        test_gender_male_list.append(test_gender_male)
        test_gender_unknown = data[15]
        test_gender_unknown_list.append(test_gender_unknown)

        test_race_latinx = data[16]
        test_race_latinx_list.append(test_race_latinx)
        test_race_asian = data[17]
        test_race_asian_list.append(test_race_asian)
        test_race_black = data[18]
        test_race_black_list.append(test_race_black)
        test_race_white = data[19]
        test_race_white_list.append(test_race_white)
        test_race_other_race = data[20]
        test_race_other_race_list.append(test_race_other_race)
        test_race_unknown = data[21]
        test_race_unknown_list.append(test_race_unknown)

        pos_test_0_17_yrs = data[22]
        pos_test_0_17_yrs_list.append(pos_test_0_17_yrs)
        pos_test_18_29_yrs = data[23]
        pos_test_18_29_yrs_list.append(pos_test_18_29_yrs)
        pos_test_30_39_yrs = data[24]
        pos_test_30_39_yrs_list.append(pos_test_30_39_yrs)
        pos_test_40_49_yrs = data[25]
        pos_test_40_49_yrs_list.append(pos_test_40_49_yrs)
        pos_test_50_59_yrs = data[26]
        pos_test_50_59_yrs_list.append(pos_test_50_59_yrs)
        pos_test_60_69_yrs = data[27]
        pos_test_60_69_yrs_list.append(pos_test_60_69_yrs)
        pos_test_70_79_yrs = data[28]
        pos_test_70_79_yrs_list.append(pos_test_70_79_yrs)
        pos_test_80yrs = data[29]
        pos_test_80yrs_list.append(pos_test_80yrs)
        pos_test_unknown_yrs = data[30]
        pos_test_unknown_yrs_list.append(pos_test_unknown_yrs)

        neg_test_0_17_yrs = data[40]
        neg_test_0_17_yrs_list.append(neg_test_0_17_yrs)
        neg_test_18_29_yrs = data[41]
        neg_test_18_29_yrs_list.append(neg_test_18_29_yrs)
        neg_test_30_39_yrs = data[42]
        neg_test_30_39_yrs_list.append(neg_test_30_39_yrs)
        neg_test_40_49_yrs = data[43]
        neg_test_40_49_yrs_list.append(neg_test_40_49_yrs)
        neg_test_50_59_yrs = data[44]
        neg_test_50_59_yrs_list.append(neg_test_50_59_yrs)
        neg_test_60_69_yrs = data[45]
        neg_test_60_69_yrs_list.append(neg_test_60_69_yrs)
        neg_test_70_79_yrs = data[46]
        neg_test_70_79_yrs_list.append(neg_test_70_79_yrs)
        neg_test_80yrs = data[47]
        neg_test_80yrs_list.append(neg_test_80yrs)
        neg_test_unknown_yrs = data[48]
        neg_test_unknown_yrs_list.append(neg_test_unknown_yrs)

        pos_test_female = data[31]
        pos_test_female_list.append(pos_test_female)
        pos_test_male = data[32]
        pos_test_male_list.append(pos_test_male)
        pos_test_unk_gender = data[33]
        pos_test_unk_gender_list.append(pos_test_unk_gender)
        neg_test_female = data[49]
        neg_test_female_list.append(neg_test_female)
        neg_test_male = data[50]
        neg_test_male_list.append(neg_test_male)
        neg_test_unk_gender = data[51]
        neg_test_unk_gender_list.append(neg_test_unk_gender)

        pos_test_latinx = data[34]
        pos_test_latinx_list.append(pos_test_latinx)
        pos_test_asian = data[35]
        pos_test_asian_list.append(pos_test_asian)
        pos_test_black = data[36]
        pos_test_black_list.append(pos_test_black)
        pos_test_white = data[37]
        pos_test_white_list.append(pos_test_white)
        pos_test_other_race = data[38]
        pos_test_other_race_list.append(pos_test_other_race)
        pos_test_race_unknown = data[39]
        pos_test_race_unknown_list.append(pos_test_race_unknown)
        neg_test_latinx = data[52]
        neg_test_latinx_list.append(neg_test_latinx)
        neg_test_asian = data[53]
        neg_test_asian_list.append(neg_test_asian)
        neg_test_black = data[54]
        neg_test_black_list.append(neg_test_black)
        neg_test_white = data[55]
        neg_test_white_list.append(neg_test_white)
        neg_test_other_race = data[56]
        neg_test_other_race_list.append(neg_test_other_race)
        neg_test_race_unknown = data[57]
        neg_test_race_unknown_list.append(neg_test_race_unknown)

        # print(pos_test)
    # print(max(i))
        # ordered_dict = sorted(covid_data, key=lambda x: datetime.strptime(i, '%m/%d/%Y')) # Sort the dictionary keys 
        # # print(ordered_dict)
        # # first_key = list(ordered.keys())[0]
        # first_key = next(iter(ordered_dict))
        # print(first_key)
        # print()
        # last_key = list(ordered_dict)[-1]
        # print(last_key)
    max_tests = max(total_test_list)
    average_test = sum(total_test_list) / len(total_test_list)
    print(f'{average_test:.0f}')
    # week_day = [1,2,3,4,5,6,7]
    print(max_tests)

    # Total tests line graph
    plt.plot(pos_test_list, label='positive tests')
    # plt.xticks(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    # labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.plot(neg_test_list, label='negative tests', linewidth=2, marker='.', markersize=10)
    plt.plot(total_test_list, label='total tests')
    plt.title('COVID-19 tests in Chicago')
    plt.xlabel('Number of days')
    plt.ylabel('Number of tests')
    plt.legend()
    plt.show()

    # Tests by age group bar chart
    labels_age_tests = ['0-17 years', '18-29years', '30-39 years', '40-49 years', '50-59 years', '60-69 years', '70-79 years', '80 years+', 'Race Unknown']
    age_tests_values = [sum(test_0_17_yrs_list), sum(test_18_29_yrs_list), sum(test_30_39_yrs_list), sum(test_40_49_yrs_list), sum(test_50_59_yrs_list), sum(test_60_69_yrs_list), sum(test_70_79_yrs_list), sum(test_80yrs_list), sum(test_unknown_yrs_list)]
    # age_tests_values1 = [1,5,9,2,3,4,6,8,9] 
    plt.bar(labels_age_tests, age_tests_values)
    plt.title('COVID-19 cumulative tests by age group in Chicago')
    plt.xlabel('Age group')
    plt.ylabel('Total tests (millions)')
    plt.show()

    # Tests by gender bar chart
    labels_gender_tests = ['Female', 'Male', 'Gender Unkwown']
    gender_tests_values = [sum(test_gender_female_list), sum(test_gender_male_list), sum(test_gender_unknown_list)]
    plt.bar(labels_gender_tests, gender_tests_values)
    plt.title('COVID-19 cumulative tests by gender groups in Chicago')
    plt.xlabel('Gender')
    plt.ylabel('Total tests (millions)')
    plt.show()

    # Tests by race bar chart
    labels_race_tests = ['Latinx', 'Asian', 'Black', 'White', 'Other', 'Race Unkown']
    race_tests_values = [sum(test_race_latinx_list), sum(test_race_asian_list), sum(test_race_black_list), sum(test_race_white_list), sum(test_race_other_race_list), sum(test_race_unknown_list)]
    plt.bar(labels_race_tests, race_tests_values)
    plt.title('COVID-19 cumulative tests by race groups in Chicago')
    plt.xlabel('Ethnicity/ Race')
    plt.ylabel('Total tests (millions)')
    plt.show()

    # Tests results by age group bar chart
    labels_age_test_results = ['0-17 years', '18-29years', '30-39 years', '40-49 years', '50-59 years', '60-69 years', '70-79 years', '80 years+', 'Age Unknown']
    pos_age_values = [sum(pos_test_0_17_yrs_list), sum(pos_test_18_29_yrs_list), sum(pos_test_30_39_yrs_list), sum(pos_test_40_49_yrs_list), sum(pos_test_50_59_yrs_list), sum(pos_test_60_69_yrs_list), sum(pos_test_70_79_yrs_list), sum(pos_test_80yrs_list), sum(pos_test_unknown_yrs_list)]
    neg_age_values = [sum(neg_test_0_17_yrs_list), sum(neg_test_18_29_yrs_list), sum(neg_test_30_39_yrs_list), sum(neg_test_40_49_yrs_list), sum(neg_test_50_59_yrs_list), sum(neg_test_60_69_yrs_list), sum(neg_test_70_79_yrs_list), sum(neg_test_80yrs_list), sum(neg_test_unknown_yrs_list)]
    plt.bar(labels_age_test_results, pos_age_values, label='COVID-19 positive results')
    plt.bar(labels_age_test_results, neg_age_values, bottom=pos_age_values, label='COVID-19 negative results')
    plt.xlabel('Test results per age group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

    # Tests results by gender bar chart
    label_gender_test_results = ['Female', 'Male', 'Gender Unkwown']
    pos_gender_values = [sum(pos_test_female_list), sum(pos_test_male_list), sum(pos_test_unk_gender_list)]
    neg_gender_values = [sum(neg_test_female_list), sum(neg_test_male_list), sum(neg_test_unk_gender_list)]
    plt.bar(label_gender_test_results, pos_gender_values, label='COVID-19 positive results')
    plt.bar(label_gender_test_results, neg_gender_values, bottom=pos_gender_values, label='COVID-19 negative results')
    plt.xlabel('Test results per gender group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

    # Tests results by race bar chart
    labels_race_test_results = ['Latinx', 'Asian', 'Black', 'White', 'Other', 'Race Unknown']
    pos_race_values = [sum(pos_test_latinx_list), sum(pos_test_asian_list), sum(pos_test_black_list), sum(pos_test_white_list), sum(pos_test_other_race_list), sum(pos_test_race_unknown_list)]
    neg_race_results = [sum(neg_test_latinx_list), sum(neg_test_asian_list), sum(neg_test_black_list), sum(neg_test_white_list), sum(neg_test_other_race_list), sum(neg_test_race_unknown_list)]
    plt.bar(labels_race_test_results, pos_race_values, label='COVID-19 positive results')
    plt.bar(labels_race_test_results, neg_race_results, bottom=pos_race_values, label='COVID-19 negative results')
    plt.xlabel('Test results per ethnic group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

    # PANDAS
    covid19 = pd.read_csv("COVID-19-Daily-tests.csv")
    print(covid19)
    # covid19.info()
    # time = [0, 1, 2, 3]
    # position = [0, 100, 200, 300]

    # plt.plot(position)
    # plt.xlabel('Time (hr)')
    # plt.ylabel('Position (km)')
    # plt.show()
    # for row in covid_data:

    #     date = row[0]
    #     tests = row[4]
    #     plt.plot(date, tests)
    #     # plt.plot(covid19)
    #     plt.show()
    # df = pd.DataFrame(np.random.covid19, 
    #               columns=('col_1', 'col_2', 'col_3', 'col_4'))
    # df.plot()
    # for j in covid_data:
    #     ordered_dict = sorted(j, key=lambda x: datetime.strptime(x, '%m/%d/%Y')) # Sort the dictionary keys 
    #     # print(ordered_dict)
    #     # first_key = list(ordered.keys())[0]
    #     first_key = next(iter(ordered_dict))
    #     print(first_key)
    #     print()
    #     last_key = list(ordered_dict)[-1]
    #     print(last_key)
    

    # first_key = next(iter(sorted_covid_data))
    # sorted_covid_data = sort_covid_data(first_key, last_key)
    
    
    # for j in sorted_covid_data:
    # print(sorted_covid_data)
    
    # plt.close("all")
    # keys = sort_covid_data()

def read_covid19(covid_dict):
    """Reads the contents of the COVID-19-Daily-tests.csv file into the dictionary named covid_dict and returns a dictionary
    Parameters:
        covid_dict: The dictionary that will be populated
    Return:
        Covid-19 dictionary
    """
    covid_dict = {}
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Retrieve items from each row in the csv file and add to the dictionary
            date = row[0]
            day = row[1]
            pos_tests = int(row[2])
            neg_tests = int(row[3])
            total_tests = int(row[4])
            test_0_17_yrs = int(row[5])
            test_18_29_yrs = int(row[6])
            test_30_39_yrs = int(row[7])
            test_40_49_yrs = int(row[8])
            test_50_59_yrs = int(row[9])
            test_60_69_yrs = int(row[10])
            test_70_79_yrs = int(row[11])
            test_80yrs = int(row[12])
            test_unknown_yrs = int(row[13])
            test_gender_female = int(row[14])
            test_gender_male = int(row[15])
            test_gender_unknown = int(row[16])
            test_race_latinx = int(row[17])
            test_race_asian = int(row[18])
            test_race_black = int(row[19])
            test_race_white = int(row[20])
            test_race_other_race = int(row[21])
            test_race_unknown = int(row[22])
            pos_test_0_17_yrs = int(row[23])
            pos_test_18_29_yrs = int(row[24])
            pos_test_30_39_yrs = int(row[25])
            pos_test_40_49_yrs = int(row[26])
            pos_test_50_59_yrs = int(row[27])
            pos_test_60_69_yrs = int(row[28])
            pos_test_70_79_yrs = int(row[29])
            pos_test_80yrs = int(row[30])
            pos_test_unknown_yrs = int(row[31])
            pos_test_female = int(row[32])
            pos_test_male = int(row[33])
            pos_test_unk_gender = int(row[34])
            pos_test_latinx = int(row[35])
            pos_test_asian = int(row[36])
            pos_test_black = int(row[37])
            pos_test_white = int(row[38])
            pos_test_other_race = int(row[39])
            pos_test_race_unknown = int(row[40])
            neg_test_0_17_yrs = int(row[41])
            neg_test_18_29_yrs = int(row[42])
            neg_test_30_39_yrs = int(row[43])
            neg_test_40_49_yrs = int(row[44])
            neg_test_50_59_yrs = int(row[45])
            neg_test_60_69_yrs = int(row[46])
            neg_test_70_79_yrs = int(row[47])
            neg_test_80yrs = int(row[48])
            neg_test_unknown_yrs = int(row[49])
            neg_test_female = int(row[50])
            neg_test_male = int(row[51])
            neg_test_unk_gender = int(row[52])
            neg_test_latinx = int(row[53])
            neg_test_asian = int(row[54])
            neg_test_black = int(row[55])
            neg_test_white = int(row[56])
            neg_test_other_race = int(row[57])
            neg_test_race_unknown = int(row[58])

            covid_dict[date] = [day, pos_tests, neg_tests, total_tests, test_0_17_yrs, test_18_29_yrs, test_30_39_yrs,\
                test_40_49_yrs, test_50_59_yrs, test_60_69_yrs, test_70_79_yrs, test_80yrs, test_unknown_yrs,\
                test_gender_female, test_gender_male, test_gender_unknown, test_race_latinx, test_race_asian, test_race_black,\
                test_race_white, test_race_other_race, test_race_unknown, pos_test_0_17_yrs, pos_test_18_29_yrs, pos_test_30_39_yrs,\
                pos_test_40_49_yrs, pos_test_50_59_yrs, pos_test_60_69_yrs, pos_test_70_79_yrs, pos_test_80yrs, \
                pos_test_unknown_yrs, pos_test_female, pos_test_male, pos_test_unk_gender, pos_test_latinx, \
                pos_test_asian, pos_test_black, pos_test_white, pos_test_other_race, pos_test_race_unknown, \
                neg_test_0_17_yrs, neg_test_18_29_yrs, neg_test_30_39_yrs, neg_test_40_49_yrs, neg_test_50_59_yrs, \
                neg_test_60_69_yrs, neg_test_70_79_yrs, neg_test_80yrs, neg_test_unknown_yrs, neg_test_female, \
                neg_test_male, neg_test_unk_gender, neg_test_latinx, neg_test_asian, neg_test_black, neg_test_white, \
                neg_test_other_race, neg_test_race_unknown]
    return covid_dict

# def sort_covid_data():
#     """Reads the contents of the COVID-19-Daily-tests.csv file into the dictionary named dictionary for sorting the keys and the returns\
#     the first and last keys of the sorted dictionary
#     Parameters:
#         dictionary: The dictionary that will be populated by calling the read_covid19() function
#     Return:
#         First and Last keys of the sorted dictionary keys
#     """

#     dictionary = read_covid19('COVID-19-Daily-tests.csv') # Call the read_covid19 function and read the csv file contents into a dictionary
#     ordered_dict = sorted(dictionary, key=lambda x: datetime.strptime(x, "%m/%d/%Y")) # Sort the dictionary keys 
#     # print(ordered_dict)
#     # first_key = list(ordered.keys())[0]
#     first_key = next(iter(ordered_dict))
#     # print(first_key)
#     print()
#     last_key = list(ordered_dict)[-1]
#     print(last_key)
    
#     # return first_key, last_key
#         # for i in dictionary:
#         #     # i = datetime.strptime(i, '%m/%d/%Y')
#         # #     dictionary.sort(key=lambda date: datetime.strptime(dictionary, '%m/%d/%Y'))
#         #     sorted_dictionary = {i: dictionary[i] for i in sorted(dictionary)}
#         # return sorted_dictionary
#         # def sortedDictValues(adict):
#         # items = dictionary.items()
#         # items.sort()
#         # return [value for key, value in items]
#     #     def printDates(dates): 
    
#     #     for i in range(len(dates)):  
#     #         print(dates[i]) 
        
        
#     # if __name__ == "__main__":  
    
#     #     dates =  ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018", 
#     #               "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]  
        
#     #     # Sort the list in ascending order of dates 
#     #     dates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
        
#     #     # Print the dates in a sorted order 
#     #     printDates(dates)
#     #     DATE_INDEX = 0
#     #     popul_func = lambda country: country[POPULATION_INDEX]

#     #     # Sort the list of countries by the population.
#     #     sorted_list = sorted(countries, key=popul_func)

#     #     # Print the sorted list.
#     #     print("List of countries sorted by population")
#     #     for country in sorted_list:
#     #         print(country)

#     #         d = {2:3, 1:89, 4:5, 3:0}

#     # s = {k : d[k] for k in sorted(d)}

#     # def plot_charts(x, y):
#     #     dictionary = read_covid19('COVID-19-Daily-tests.csv')
#     #     data = 


if __name__ == '__main__':
    main()

