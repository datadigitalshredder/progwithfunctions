from week13_covid19analysis_chicago import read_covid19, plot_overall_tests, plot_age_group_tests, plot_gender_tests, plot_race_tests, plot_age_group_results, \
    plot_gender_results, plot_ethnicity_results, positivity_rate_age, positivity_rate_gender, positivity_rate_race 
import pytest
from pytest import approx
import csv
# from datetime import datetime

def test_read_covid19():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        covid_dictionary = read_covid19(covid)
        for i in covid_dictionary:
            length_key = len(covid_dictionary[i])
            
            assert length_key == 58 # check the number of columns of the value pairs
            assert len(covid_dictionary) == 633 # check the number rows in the dictionary
        
            # date_format = datetime.strptime(dates, '%m/%d/%Y')
            
            # datetime.strptime(dates, date_format)
            # assert date_format == i
            # stripped_date = datetime.strptime(i, '%m/%d/%Y')
            # assert stripped_date == datetime(i)
            # print("This is the correct date string format.")
            # except ValueError:
            #     print("This is the incorrect date string format. It should be YYYY-MM-DD")
def test_plot_overall_tests():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        pos_test_list = []
        neg_test_list = []
        total_test_list = []
        for row in reader:
            # Retrieve items from each row in the csv file
            date = row[0]
            day = row[1]
            pos_tests = int(row[2])
            pos_test_list.append(pos_tests)
            neg_tests = int(row[3])
            neg_test_list.append(neg_tests)
            total_tests = int(row[4])
            total_test_list.append(total_tests)

            sum_pos_tests = sum(pos_test_list)
            sum_neg_tests = sum(neg_test_list)
            
        assert sum_pos_tests + sum_neg_tests == approx(sum(total_test_list), 0.01)
        assert pos_tests + neg_tests == approx(total_tests, 0.01)

def test_plot_age_group_tests():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
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
        assert test_0_17_yrs + test_18_29_yrs + test_30_39_yrs + test_40_49_yrs + test_50_59_yrs + test_60_69_yrs + test_70_79_yrs + test_80yrs + test_unknown_yrs == total_tests

def test_plot_gender_tests():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            total_tests = int(row[4])
            test_gender_female = int(row[14])
            test_gender_male = int(row[15])
            test_gender_unknown = int(row[16])
        assert test_gender_female + test_gender_male + test_gender_unknown == total_tests

def test_plot_race_tests():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            total_tests = int(row[4])
            test_race_latinx = int(row[17])
            test_race_asian = int(row[18])
            test_race_black = int(row[19])
            test_race_white = int(row[20])
            test_race_other_race = int(row[21])
            test_race_unknown = int(row[22])
        assert test_race_latinx + test_race_asian + test_race_black + test_race_white + test_race_other_race + test_race_unknown == total_tests

def test_plot_age_group_results():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            total_tests = int(row[4])
            pos_test_0_17_yrs = int(row[23])
            pos_test_18_29_yrs = int(row[24])
            pos_test_30_39_yrs = int(row[25])
            pos_test_40_49_yrs = int(row[26])
            pos_test_50_59_yrs = int(row[27])
            pos_test_60_69_yrs = int(row[28])
            pos_test_70_79_yrs = int(row[29])
            pos_test_80yrs = int(row[30])
            pos_test_unknown_yrs = int(row[31])
            neg_test_0_17_yrs = int(row[41])
            neg_test_18_29_yrs = int(row[42])
            neg_test_30_39_yrs = int(row[43])
            neg_test_40_49_yrs = int(row[44])
            neg_test_50_59_yrs = int(row[45])
            neg_test_60_69_yrs = int(row[46])
            neg_test_70_79_yrs = int(row[47])
            neg_test_80yrs = int(row[48])
            neg_test_unknown_yrs = int(row[49]) 
        assert pos_test_0_17_yrs +  pos_test_18_29_yrs + pos_test_30_39_yrs + pos_test_40_49_yrs + pos_test_50_59_yrs + pos_test_60_69_yrs + pos_test_70_79_yrs + pos_test_80yrs + pos_test_unknown_yrs +\
            neg_test_0_17_yrs + neg_test_18_29_yrs + neg_test_30_39_yrs + neg_test_40_49_yrs + neg_test_50_59_yrs + neg_test_60_69_yrs + neg_test_70_79_yrs + neg_test_80yrs + \
            neg_test_unknown_yrs == total_tests

def test_plot_gender_results():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            total_tests = int(row[4])
            pos_test_female = int(row[32])
            pos_test_male = int(row[33])
            pos_test_unk_gender = int(row[34])
            neg_test_female = int(row[50])
            neg_test_male = int(row[51])
            neg_test_unk_gender = int(row[52])
        assert pos_test_female + pos_test_male + pos_test_unk_gender + neg_test_female + neg_test_male + neg_test_unk_gender == total_tests

def test_plot_ethnicity_results():
    with open('COVID-19-Daily-tests.csv', 'rt') as covid:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            total_tests = int(row[4])
            pos_test_latinx = int(row[35])
            pos_test_asian = int(row[36])
            pos_test_black = int(row[37])
            pos_test_white = int(row[38])
            pos_test_other_race = int(row[39])
            pos_test_race_unknown = int(row[40])
            neg_test_latinx = int(row[53])
            neg_test_asian = int(row[54])
            neg_test_black = int(row[55])
            neg_test_white = int(row[56])
            neg_test_other_race = int(row[57])
            neg_test_race_unknown = int(row[58])
        assert pos_test_latinx + pos_test_asian + pos_test_black + pos_test_white + pos_test_other_race + pos_test_race_unknown + neg_test_latinx + neg_test_asian + neg_test_black +\
            neg_test_white + neg_test_other_race + neg_test_race_unknown == total_tests

def test_positivity_rate_age():
    with open('COVID-19-Daily-tests-modified.csv', 'rt') as covid_mod:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid_mod)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            pos_tests = int(row[2])
            total_tests = int(row[4])
            pos_rate = float(row[59])
        assert (pos_tests / total_tests) * 100 == pos_rate

def test_positivity_rate_gender():
    with open('COVID-19-Daily-tests-modified.csv', 'rt') as covid_mod:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid_mod)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            pos_test_female = int(row[32])
            pos_test_male = int(row[33])
            pos_test_unk_gender = int(row[34])
            total_tests = int(row[4])
            pos_rate = float(row[59])
        assert ((pos_test_female + pos_test_male + pos_test_unk_gender) / total_tests) * 100 == pos_rate

def test_positivity_rate_race():
    with open('COVID-19-Daily-tests-modified.csv', 'rt') as covid_mod:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(covid_mod)

        # The first line of the CSV file contains column headings,
        # so this statement skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Retrieve items from each row in the csv file
            pos_test_latinx = int(row[35])
            pos_test_asian = int(row[36])
            pos_test_black = int(row[37])
            pos_test_white = int(row[38])
            pos_test_other_race = int(row[39])
            pos_test_race_unknown = int(row[40])
            total_tests = int(row[4])
            pos_rate = float(row[59])
        assert ((pos_test_latinx + pos_test_asian + pos_test_black + pos_test_white + pos_test_other_race + pos_test_race_unknown) / total_tests) * 100 == pos_rate


pytest.main(["-v", "--tb=line", "-rN", __file__])
