# import numpy as np
import pandas as pd
import csv
# from datetime import datetime
import matplotlib.pyplot as plt

def main():
    try:
        print()
        print('You are about to visualize data for the COVID-19 tests (retrieved Nov 26, 2021 on https://catalog.data.gov/dataset/covid-19-daily-testing-by-test) for City of Chicago residents.')
        print()
        print('The file is a csv file and the dataFrame summary is as follows:')


        covid_data = read_covid19('COVID-19-Daily-tests.csv')

        data_summary = data_analysis(covid_data)

        df = pd.read_csv("COVID-19-Daily-tests-modified.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        
        date_info = input('Enter date in the format YYYY-MM-DD between 2020-03-01 to 2021-11-23: ')
        print()
        # try: 
        # date_info_format = f'{date_info:%Y %m %d}'
        # print(date_info)
        # print(df[df[‘Name’]==’Donna’].index.values)
        date_index = (df[df['Date'] == date_info].index.values)
        # date_index_match = df['Date'] == date_info
        # date_indexxx = df[date_index_match].index.values
        # date_index1 = df.loc[df['Date']==date_info]
        # print(date_index) 
        total_test = df.iloc[date_index,4]
        # total_test2 = df.iloc[total_test,4]
        # total_test1 = df.iloc[632,4]
        positivity_rate = df.iloc[date_index,59]
        # positivity_rate1 = df.iloc[632,59]
        # except TypeError as type_error:
        #     print(f"{type_error} That's an invalid date format Try again.")
        # except ValueError as value_error:
        #     print(f"{value_error} That's an invalid date format Try again.")

        # print(date_index1)
        print(f'On {date_info}, \nThe total number of tests were \nIndex: Total tests: \n{total_test}') 
        print(f'\nThe positivity rate was \nIndex: Positivity rate: \n{positivity_rate}')
        print()
        # print(f'On {date_info}, there were {df.iloc[date_index,4]} total tests with a positivity rate of {df.iloc[date_index,59]}.')


        #User input
        # max_tests = max(total_test_list)
        # average_test = sum(total_test_list) / len(total_test_list)
        # print(f'{average_test:.0f}')
        # # week_day = [1,2,3,4,5,6,7]
        # print(max_tests)
        # data_summary = data_analysis(covid_data)

        view_data = input('There are ten charts and graphs. Do you want to visualize the data (Y/N)? ')
        print()
        if view_data.lower() == 'y':

            # covid_data = read_covid19('COVID-19-Daily-tests.csv')

            # data_summary = data_analysis(covid_data)
            tests_plot = plot_overall_tests(covid_data)
            age_group_plot = plot_age_group_tests(covid_data)
            gender_type_plot = plot_gender_tests(covid_data)
            ethnicity_tests_plot = plot_race_tests(covid_data)
            age_test_results_plot = plot_age_group_results(covid_data)
            gender_test_results_plot = plot_gender_results(covid_data)
            ethnicity_test_results_plot = plot_ethnicity_results(covid_data)

            positivity_rate_ages = positivity_rate_age()
            positivity_rate_gender_type = positivity_rate_gender()
            positivity_rate_ethnicity = positivity_rate_race()
            print('Thank you for taking a moment to learn about Covid-19 in the City of Chicago. \nHopefully you were able to draw some conclusions from the data. \nGood bye')
            print()
        else:
            print('Thank you for taking a moment to learn about Covid-19 in the City of Chicago. \nGood bye')
            print()
    except FileNotFoundError as not_found:
        print(f'{not_found}.\nThe file you entered was not found. \nPlease make sure the file COVID-19-Daily-tests.csv is in the some location as the python file.')
    
    except PermissionError as perm_error:
        print(f'{perm_error}. \nYou do not have permission to access this file.')

    except KeyError as key_error:
        print(f'{key_error}. \nThe key entered is not on the store list.')

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

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
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

            # Populate the dictionary
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

# MATPLOTLIB GRAPHS
def plot_overall_tests(covid_data):
    """Creates and populates lists of overal, positive, and negative test results, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
    # Create empty list to populate
    pos_test_list = []
    neg_test_list = []
    total_test_list = []

    # Iterate through each row in the dictionary and from each row retrieve the data and add to the list
    for i in covid_data:
        data = covid_data[i]
        pos_test = data[1]
        pos_test_list.append(pos_test)
        neg_test = data[2]
        neg_test_list.append(neg_test)
        total_test = data[3]
        total_test_list.append(total_test)

    # Total tests line graph
    plt.plot(pos_test_list, label='positive')
    plt.plot(neg_test_list, label='negative', linewidth=2, marker='.', markersize=10)
    plt.plot(total_test_list, label='total tests')
    plt.title('COVID-19 tests in Chicago')
    plt.xlabel('Number of days')
    plt.ylabel('Number of tests')
    plt.legend()
    plt.show()
    # check = sum(pos_test_list)
    # print(check)

def plot_age_group_tests(covid_data):
    """Creates and populates lists of tests by age group, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
    test_0_17_yrs_list = []
    test_18_29_yrs_list = []
    test_30_39_yrs_list = []
    test_40_49_yrs_list = []
    test_50_59_yrs_list = []
    test_60_69_yrs_list = []
    test_70_79_yrs_list = []
    test_80yrs_list = []
    test_unknown_yrs_list = []
    for i in covid_data:
        data = covid_data[i]
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

    # Tests by age group bar chart
    labels_age_tests = ['0-17 years', '18-29years', '30-39 years', '40-49 years', '50-59 years', '60-69 years', '70-79 years', '80 years+', 'Age Unknown']
    age_tests_values = [sum(test_0_17_yrs_list), sum(test_18_29_yrs_list), sum(test_30_39_yrs_list), sum(test_40_49_yrs_list), sum(test_50_59_yrs_list), sum(test_60_69_yrs_list), sum(test_70_79_yrs_list), sum(test_80yrs_list), sum(test_unknown_yrs_list)]
    plt.bar(labels_age_tests, age_tests_values)
    plt.title('COVID-19 cumulative tests by age group in Chicago')
    plt.xlabel('Age group')
    plt.ylabel('Total tests (millions)')
    plt.show()

def plot_gender_tests(covid_data):
    """Creates and populates lists of tests by gender, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
    test_gender_female_list = []
    test_gender_male_list = []
    test_gender_unknown_list = []
    for i in covid_data:
        data = covid_data[i]
        test_gender_female = data[13]
        test_gender_female_list.append(test_gender_female)
        test_gender_male = data[14]
        test_gender_male_list.append(test_gender_male)
        test_gender_unknown = data[15]
        test_gender_unknown_list.append(test_gender_unknown)

    # Tests by gender bar chart
    labels_gender_tests = ['Female', 'Male', 'Gender Unkwown']
    gender_tests_values = [sum(test_gender_female_list), sum(test_gender_male_list), sum(test_gender_unknown_list)]
    plt.bar(labels_gender_tests, gender_tests_values)
    plt.title('COVID-19 cumulative tests by gender groups in Chicago')
    plt.xlabel('Gender')
    plt.ylabel('Total tests (millions)')
    plt.show()

def plot_race_tests(covid_data):
    """Creates and populates lists of tests by ethnicity/ race, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
    test_race_latinx_list = []
    test_race_asian_list = []
    test_race_black_list = []
    test_race_white_list = []
    test_race_other_race_list = []
    test_race_unknown_list = []
    for i in covid_data:
        data = covid_data[i]
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
    # Tests by race bar chart
    labels_race_tests = ['Latinx', 'Asian', 'Black', 'White', 'Other', 'Race Unkown']
    race_tests_values = [sum(test_race_latinx_list), sum(test_race_asian_list), sum(test_race_black_list), sum(test_race_white_list), sum(test_race_other_race_list), sum(test_race_unknown_list)]
    plt.bar(labels_race_tests, race_tests_values)
    plt.title('COVID-19 cumulative tests by ethinic groups in Chicago')
    plt.xlabel('Ethnicity/ Race')
    plt.ylabel('Total tests (millions)')
    plt.show()

def plot_age_group_results(covid_data):
    """Creates and populates lists of tests results by age group, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
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
    for i in covid_data:
        data = covid_data[i]
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

    # Tests results by age group bar chart
    labels_age_test_results = ['0-17 years', '18-29years', '30-39 years', '40-49 years', '50-59 years', '60-69 years', '70-79 years', '80 years+', 'Age Unknown']
    pos_age_values = [sum(pos_test_0_17_yrs_list), sum(pos_test_18_29_yrs_list), sum(pos_test_30_39_yrs_list), sum(pos_test_40_49_yrs_list), sum(pos_test_50_59_yrs_list), sum(pos_test_60_69_yrs_list), sum(pos_test_70_79_yrs_list), sum(pos_test_80yrs_list), sum(pos_test_unknown_yrs_list)]
    neg_age_values = [sum(neg_test_0_17_yrs_list), sum(neg_test_18_29_yrs_list), sum(neg_test_30_39_yrs_list), sum(neg_test_40_49_yrs_list), sum(neg_test_50_59_yrs_list), sum(neg_test_60_69_yrs_list), sum(neg_test_70_79_yrs_list), sum(neg_test_80yrs_list), sum(neg_test_unknown_yrs_list)]
    plt.bar(labels_age_test_results, pos_age_values, label='COVID-19 positive results')
    plt.bar(labels_age_test_results, neg_age_values, bottom=pos_age_values, label='COVID-19 negative results')
    plt.title('Test results by age group in Chicago')
    plt.xlabel('Test results per age group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

def plot_gender_results(covid_data):
    """Creates and populates lists of tests results by gender, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
    pos_test_female_list = []
    pos_test_male_list = []
    pos_test_unk_gender_list = []

    neg_test_female_list = []
    neg_test_male_list = []
    neg_test_unk_gender_list = []
    for i in covid_data:
        data = covid_data[i]
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

    # Tests results by gender bar chart
    label_gender_test_results = ['Female', 'Male', 'Gender Unkwown']
    pos_gender_values = [sum(pos_test_female_list), sum(pos_test_male_list), sum(pos_test_unk_gender_list)]
    neg_gender_values = [sum(neg_test_female_list), sum(neg_test_male_list), sum(neg_test_unk_gender_list)]
    plt.bar(label_gender_test_results, pos_gender_values, label='COVID-19 positive results')
    plt.bar(label_gender_test_results, neg_gender_values, bottom=pos_gender_values, label='COVID-19 negative results')
    plt.title('Test results by gender in Chicago')
    plt.xlabel('Test results per gender group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

def plot_ethnicity_results(covid_data):
    """Creates and populates lists of tests results by ethnicity/ race, and plots the graph
    Parameters:
        A dictionary with Covid-19 data
    Return value:
        None
    """
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
    # Tests results by race bar chart
    labels_race_test_results = ['Latinx', 'Asian', 'Black', 'White', 'Other', 'Race Unknown']
    pos_race_values = [sum(pos_test_latinx_list), sum(pos_test_asian_list), sum(pos_test_black_list), sum(pos_test_white_list), sum(pos_test_other_race_list), sum(pos_test_race_unknown_list)]
    neg_race_results = [sum(neg_test_latinx_list), sum(neg_test_asian_list), sum(neg_test_black_list), sum(neg_test_white_list), sum(neg_test_other_race_list), sum(neg_test_race_unknown_list)]
    plt.bar(labels_race_test_results, pos_race_values, label='COVID-19 positive results')
    plt.bar(labels_race_test_results, neg_race_results, bottom=pos_race_values, label='COVID-19 negative results')
    plt.title('Test results by ethnic group in Chicago')
    plt.xlabel('Test results per ethnic group')
    plt.ylabel('Total tests (millions)')
    plt.legend()
    plt.show()

# PANDAS
def data_analysis(df):
    df = pd.read_csv("COVID-19-Daily-tests.csv")
    # print(covid19)
    df.info()
    # print(df.head(5))
    # print(df.tail(5))
    # coviddata.info()
    # print(coviddata)
    # sorts = df.sort_values('Date')
    # print(sorts.head(5))
    # print(sorts.tail(5))

    # CODE TO CONVERT THE DATE STRING TO A DATETIME STRING
    # checking datatype
    # print(type(df.Date[0]))
    
    # convert to date
    df['Date'] = pd.to_datetime(df['Date'])
    
    # verify datatype
    # print(type(df.Date[0]))

    # Sort the data by dates
    df = df.sort_values(by='Date')
    
    first_day = df.iloc[0,0] # Get the first date in sorted dataFrame
    last_day = df.iloc[632,0] # Get the last date in the sorted dataFrame
    print()
    print(f'The data set is from {first_day:%a %b %d, %Y} to {last_day:%a %b %d, %Y}.')
    print()
    # print(sorts.describe()) # Get the data summary
    print(f'A total of {last_day - first_day} of COVID-19 test results.')
    print()
    print(df.head(5))
    print()


    # Making changes to the dataFrame
    # Add Positivity Rate columns to each category in the data set
    # Add Positivity Rate column to Overal tests
    df['Overal Positivity Rate'] = (df['Positive Tests'] / df['Total Tests']) * 100

    # Add Positivity Rate column to age group tests
    df['0-17 years Positivity Rate'] = (df['Positive Tests - Age 0-17'] / df['Tests - Age 0-17']) * 100
    df['18-29 years Positivity Rate'] = (df['Positive Tests - Age 18-29'] / df['Tests - Age 18-29']) * 100
    df['30-39 years Positivity Rate'] = (df['Positive Tests - Age 30-39'] / df['Tests - Age 30-39']) * 100
    df['40-49 years Positivity Rate'] = (df['Positive Tests - Age 40-49'] / df['Tests - Age 40-49']) * 100
    df['50-59 years Positivity Rate'] = (df['Positive Tests - Age 50-59'] / df['Tests - Age 50-59']) * 100
    df['60-69 years Positivity Rate'] = (df['Positive Tests - Age 60-69'] / df['Tests - Age 60-69']) * 100
    df['70-79 years Positivity Rate'] = (df['Positive Tests - Age 70-79'] / df['Tests - Age 70-79']) * 100
    df['80+ years Positivity Rate'] = (df['Positive Tests - Age 80+'] / df['Tests - Age 80+']) * 100
    df['Age Unknown Positivity Rate'] = (df['Positive Tests - Age Unknown'] / df['Tests - Age Unknown']) * 100

    # Add Positivity Rate column to gender group tests
    df['Female Positivity Rate'] = (df['Positive Tests - Female'] / df['Tests - Female']) * 100
    df['Male Positivity Rate'] = (df['Positive Tests - Male'] / df['Tests - Male']) * 100
    df['Gender Unknown Positivity Rate'] = (df['Positive Tests - Unknown Gender'] / df['Tests - Gender Unknown']) * 100

    # Add Positivity Rate column to ethnicity group tests
    df['Latinx Positivity Rate'] = (df['Positive Tests - Latinx'] / df['Tests - Latinx']) * 100
    df['Asian Positivity Rate'] = (df['Positive Tests - Asian Non-Latinx'] / df['Tests - Asian Non-Latinx']) * 100
    df['Black Positivity Rate'] = (df['Positive Tests - Black Non-Latinx'] / df['Tests - Black Non-Latinx']) * 100
    df['White Positivity Rate'] = (df['Positive Tests - White Non-Latinx'] / df['Tests - White Non-Latinx']) * 100
    df['Other Race Positivity Rate'] = (df['Positive Tests - Other Race Non-Latinx'] / df['Tests - Other Race Non-Latinx']) * 100
    df['Unknown Race Positivity Rate'] = (df['Positive Tests - Unknown Race/Ethnicity'] / df['Tests - Unknown Race/Ethnicity']) * 100

    # Save the new csv file
    df.to_csv('COVID-19-Daily-tests-modified.csv', index=False)

# Plot the Age group positivity rates
def positivity_rate_age():
    """Reads the modified csv file and extracts age group positivity rates and plots the line graphs
    Parameters:
        None
    Return value:
        None
    """
    df = pd.read_csv('COVID-19-Daily-tests-modified.csv')
    # pos_rates_values = df['Overal Positivity Rate']
    pos_rates_0_17_years = df['0-17 years Positivity Rate']
    pos_rates_18_29_years =  df['18-29 years Positivity Rate']
    pos_rates_30_39_years =  df['30-39 years Positivity Rate']
    pos_rates_40_49_years =  df['40-49 years Positivity Rate']
    pos_rates_50_59_years =  df['50-59 years Positivity Rate']
    pos_rates_60_69_years =  df['60-69 years Positivity Rate']
    pos_rates_70_79_years =  df['70-79 years Positivity Rate']
    pos_rates_80_years =  df['80+ years Positivity Rate']
    pos_rates_unknown_years =  df['Age Unknown Positivity Rate']

    # plt.plot(pos_rates_values, label='overal positivity rates')
    plt.plot(pos_rates_0_17_years, label='0-17 years')
    plt.plot(pos_rates_18_29_years, label='18-29 years')
    plt.plot(pos_rates_30_39_years, label='30-39 years')
    plt.plot(pos_rates_40_49_years, label='40-49 years')
    plt.plot(pos_rates_50_59_years, label='50-59 years')
    plt.plot(pos_rates_60_69_years, label='60-69 years')
    plt.plot(pos_rates_70_79_years, label='70-79 years')
    plt.plot(pos_rates_80_years, label='80+ years')
    plt.plot(pos_rates_unknown_years, label='Age Unknown')

    plt.title('Positivity rates by age in Chicago')
    plt.xlabel('Number of days')
    plt.ylabel('Positivity rate')
    plt.legend()
    plt.show()

# Plot the Gender group positivity rates
def positivity_rate_gender():
    """Reads the modified csv file and extracts gender positivity rates and plots the line graphs
    Parameters:
        None
    Return value:
        None
    """
    df = pd.read_csv('COVID-19-Daily-tests-modified.csv')
    # pos_rates_values = df['Overal Positivity Rate']
    pos_rates_female = df['Female Positivity Rate']
    pos_rates_male =  df['Male Positivity Rate']
    pos_rates_gender_unknown =  df['Gender Unknown Positivity Rate']


    # plt.plot(pos_rates_values, label='overal positivity rates')
    plt.plot(pos_rates_female, label='female')
    plt.plot(pos_rates_male, label='male')
    plt.plot(pos_rates_gender_unknown, label='unknown gender')
    
    plt.title('Positivity rates by gender in Chicago')
    plt.xlabel('Number of days')
    plt.ylabel('Positivity rate')
    plt.legend()
    plt.show()  
    
# Plot the Ethnicity group positivity rates
def positivity_rate_race():
    """Reads the modified csv file and extracts ethnicity positivity rate and plots the line graphs
    Parameters:
        None
    Return value:
        None
    """
    df = pd.read_csv('COVID-19-Daily-tests-modified.csv')
    pos_rates_latinx = df['Latinx Positivity Rate']
    pos_rates_asian =  df['Asian Positivity Rate']
    pos_rates_black =  df['Black Positivity Rate']
    pos_rates_white =  df['White Positivity Rate']
    pos_rates_other =  df['Other Race Positivity Rate']
    pos_rates_unknown_race =  df['Unknown Race Positivity Rate']

    plt.plot(pos_rates_latinx, label='Latinx')
    plt.plot(pos_rates_asian, label='Asian')
    plt.plot(pos_rates_black, label='Black')
    plt.plot(pos_rates_white, label='White')
    plt.plot(pos_rates_other, label='Other Race')
    plt.plot(pos_rates_unknown_race, label='Unknown Race')

    plt.title('Positivity rate by ethnicity in Chicago')
    plt.xlabel('Number of days')
    plt.ylabel('Positivity rate')
    plt.legend()
    plt.show()  
    # print(df.head(5))

    # print(df.columns)
  
if __name__ == '__main__':
    main()