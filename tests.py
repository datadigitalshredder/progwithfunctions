# print('tests')
# a = 1
# b = 3
# c = -2
# result = a + b * 7 % 4 - c
# print(result)

# d = 2
# e = 2
# print(d + e)

# s = f"You found {c} coins."
# print(s)

# import random
# names=["We","I","They","He","She","Jack","Jim"]
# verbs=["was","is","are","were"]
# nouns=["playing a game","watching television","talking","dancing","speaking"]
# while True:
#     a=(random.choice(names))
#     b=(random.choice(verbs))
#     c=(random.choice(nouns))
#     print(a+" ",b+" ",c)
#     break
# while True:
#     a=(random.choice(names))
#     b=(random.choice(verbs))
#     c=(random.choice(nouns))
#     print(a+" ",b+" ",c)
#     break

# a = [1, 2, 3]
# b = [4, 5, 6]
# total = sum(a + b)
# print(total)

# mydict = { 
#     '2000-01-01': [fld_1:1, fld_2: 42], '2000-01-02': {fld_1:23, fld_2: 22.17} 
# def sortedDictValues(adict):
#  items = adict.items()
#  items.sort()
#  return [value for key, value in items]

# from collections import OrderedDict
# from datetime import datetime
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# def main():
#     my_dict = {
#         '10/18/2021':['Monday',413,29702,30115,10125,5121,4833,3492,2887,2021,986,635,15,15983,13663,469,5793,1626,5852,8037,2770,6037,107,67,69,73,48,30,9,10,0,222,190,1,87,15,86,116,43,66,10018,5054,4764,3419,2839,1991,977,625,15,15761,13473,468,5706,1611,5766,7921,2727,5971],
#         '8/8/2021':['Sunday',292,7010,7302,817,1932,1594,1205,839,470,280,161,4,3987,3286,29,744,347,1033,1755,266,3157,47,78,66,35,26,13,18,8,1,165,126,1,59,9,78,96,20,30,770,1854,1528,1170,813,457,262,153,3,3822,3160,28,685,338,955,1659,246,3127],
#         '7/7/2021':['Wednesday',95,9182,9277,1060,2005,1917,1341,1217,912,499,321,5,4852,4305,120,1172,500,2067,1928,309,3301,21,24,23,12,7,3,4,0,1,62,32,1,23,2,24,27,4,15,1039,1981,1894,1329,1210,909,495,321,4,4790,4273,119,1149,498,2043,1901,305,3286],
#         '5/15/2020':['Friday',1161,5526,6687,355,1170,1171,1075,1095,895,503,413,10,3634,2914,139,1763,102,1142,851,174,2655,81,220,231,202,175,134,73,44,1,631,521,9,635,20,208,116,29,153,274,950,940,873,920,761,430,369,9,3003,2393,130,1128,82,934,735,145,2502],
#         '4/26/2020':['Sunday',443,1342,1785,94,321,336,263,287,257,125,100,2,947,830,8,377,58,356,310,44,640,13,81,58,84,76,56,35,40,0,237,206,0,169,17,93,63,16,85,81,240,278,179,211,201,90,60,2,710,624,8,208,41,263,247,28,555],
#         '5/17/2020':['Sunday',371,2150,2521,140,392,431,357,427,403,218,150,3,1310,1175,36,473,44,609,432,90,873,18,61,66,45,75,49,25,32,0,186,184,1,181,9,88,43,11,39,122,331,365,312,352,354,193,118,3,1124,991,35,292,35,521,389,79,834],
#         '6/29/2021':['Tuesday',65,8080,8145,865,1826,1723,1260,1144,793,347,187,0,4301,3738,106,939,482,1659,1516,401,3148,16,13,14,9,1,7,4,1,0,33,32,0,17,1,20,16,3,8,849,1813,1709,1251,1143,786,343,186,0,4268,3706,106,922,481,1639,1500,398,3140],
#         '3/10/2021':['Wednesday',369,14034,14403,862,4707,2794,1842,1658,1438,667,427,8,7533,6532,338,1873,802,2972,3915,671,4170,59,110,62,46,47,23,12,9,1,180,189,0,113,12,65,121,17,41,803,4597,2732,1796,1611,1415,655,418,7,7353,6343,338,1760,790,2907,3794,654,4129],
#         '6/7/2021':['Monday',112,11656,11768,1229,2539,2174,1756,1559,1311,699,487,14,6251,5428,89,1494,648,2455,2272,458,4441,20,20,14,19,18,12,7,2,0,57,55,0,32,3,42,27,1,7,1209,2519,2160,1737,1541,1299,692,485,14,6194,5373,89,1462,645,2413,2245,457,4434]
#     }

#     ordered_dictionary = ordered_dict(my_dict)
#     print(ordered_dictionary)

# def ordered_dict(dictionary):
#     ordered = sorted(dictionary, key=lambda x: datetime.strptime(x[1], "%m/%d/%Y"))
# # 13
# # [('file4', '03/07/1998'), ('file3', '14/02/1999'), ('file1', '10/11/2000'), ('file2', '01/01/2001')]
#     # ordered = OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))
#     return ordered
# # print(ordered)
# main()

# my_dict = {
#         '10/18/2021':['Monday',413,29702,30115,10125,5121,4833,3492,2887,2021,986,635,15,15983,13663,469,5793,1626,5852,8037,2770,6037,107,67,69,73,48,30,9,10,0,222,190,1,87,15,86,116,43,66,10018,5054,4764,3419,2839,1991,977,625,15,15761,13473,468,5706,1611,5766,7921,2727,5971],
#         '8/8/2021':['Sunday',292,7010,7302,817,1932,1594,1205,839,470,280,161,4,3987,3286,29,744,347,1033,1755,266,3157,47,78,66,35,26,13,18,8,1,165,126,1,59,9,78,96,20,30,770,1854,1528,1170,813,457,262,153,3,3822,3160,28,685,338,955,1659,246,3127],
#         '7/7/2021':['Wednesday',95,9182,9277,1060,2005,1917,1341,1217,912,499,321,5,4852,4305,120,1172,500,2067,1928,309,3301,21,24,23,12,7,3,4,0,1,62,32,1,23,2,24,27,4,15,1039,1981,1894,1329,1210,909,495,321,4,4790,4273,119,1149,498,2043,1901,305,3286],
#         '05/15/2020':['Friday',1161,5526,6687,355,1170,1171,1075,1095,895,503,413,10,3634,2914,139,1763,102,1142,851,174,2655,81,220,231,202,175,134,73,44,1,631,521,9,635,20,208,116,29,153,274,950,940,873,920,761,430,369,9,3003,2393,130,1128,82,934,735,145,2502],
#         '04/26/2020':['Sunday',443,1342,1785,94,321,336,263,287,257,125,100,2,947,830,8,377,58,356,310,44,640,13,81,58,84,76,56,35,40,0,237,206,0,169,17,93,63,16,85,81,240,278,179,211,201,90,60,2,710,624,8,208,41,263,247,28,555],
#         '05/17/2020':['Sunday',371,2150,2521,140,392,431,357,427,403,218,150,3,1310,1175,36,473,44,609,432,90,873,18,61,66,45,75,49,25,32,0,186,184,1,181,9,88,43,11,39,122,331,365,312,352,354,193,118,3,1124,991,35,292,35,521,389,79,834],
#         '6/29/2021':['Tuesday',65,8080,8145,865,1826,1723,1260,1144,793,347,187,0,4301,3738,106,939,482,1659,1516,401,3148,16,13,14,9,1,7,4,1,0,33,32,0,17,1,20,16,3,8,849,1813,1709,1251,1143,786,343,186,0,4268,3706,106,922,481,1639,1500,398,3140],
#         '3/10/2021':['Wednesday',369,14034,14403,862,4707,2794,1842,1658,1438,667,427,8,7533,6532,338,1873,802,2972,3915,671,4170,59,110,62,46,47,23,12,9,1,180,189,0,113,12,65,121,17,41,803,4597,2732,1796,1611,1415,655,418,7,7353,6343,338,1760,790,2907,3794,654,4129],
#         '6/7/2021':['Monday',112,11656,11768,1229,2539,2174,1756,1559,1311,699,487,14,6251,5428,89,1494,648,2455,2272,458,4441,20,20,14,19,18,12,7,2,0,57,55,0,32,3,42,27,1,7,1209,2519,2160,1737,1541,1299,692,485,14,6194,5373,89,1462,645,2413,2245,457,4434]
#     }
# ordered = sorted(my_dict, key=lambda x: datetime.strptime(x[1], "%m/%d/%Y"))
# print(ordered)
# sorted2 = sorted(my_dict)

# xs = [('file3', '14/02/1999'), ('file1', '10/11/2000'), ('file4', '03/07/1998'), ('file2', '01/01/2001')]
# # [ (k, datetime.strptime(v, "%d/%m/%Y")) for (k,v) in xs ]
# # [('file3', datetime(1999, 2, 14, 0, 0)), ('file1', datetime(2000, 11, 10, 0, 0)), ('file4', datetime(1998, 7, 3, 0, 0)), ('file2', datetime(2001, 1, 1, 0, 0))]
# # sorted_xs = sorted(xs, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
# # print(xs)
# # [('file3', datetime.datetime(1999, 2, 14, 0, 0)), ('file1', datetime.datetime(2000, 11, 10, 0, 0)), ('file4', datetime.datetime(1998, 7, 3, 0, 0)), ('file2', datetime.datetime(2001, 1, 1, 0, 0))]
# sorted1 = sorted(xs)
# print(xs)
# print(sorted1)
# print(my_dict)
# print(sorted2)
# for i in sorted2:
    
#     print(i)

# # Example 1, Sorting a dictionary
# xs = [('file3', '14/02/1999'), ('file1', '10/11/2000'), ('file4', '03/07/1998'), ('file2', '01/01/2001')]
# print(xs)
# print()
# xs1 = sorted(xs)
# print(xs1)
# print()
# xs2 = sorted(xs, key=lambda x: x[1])
# print(xs2)
# print()
# # from datetime import datetime
# # xs3 = [ (k, datetime.strptime(v, "%d/%m/%Y")) for (k,v) in xs ]
# # print(xs3)
# # print()
# xs4 = sorted(xs, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
# print(xs4)

# # xss = [('14/02/1999','file3'), ('10/11/2000','file1'), ('03/07/1998','file4'), ('01/01/2001','file2')]
# # xss3 = [ (v, datetime.strptime(k, "%d/%m/%Y")) for (v,k) in xss ]
# # print(xss3)
# print()
# # xss4 = sorted(xss, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
# # print(xss4)

# Example 2, Sorting a dictionary
# def main():
#     dict = dictionary()
#     # print(dict)
#     """The call to main"""

# def dictionary():
#     my_dict = {
#         '10/18/2021':['Monday',413,29702,30115,10125,5121,4833,3492,2887,2021,986,635,15,15983,13663,469,5793,1626,5852,8037,2770,6037,107,67,69,73,48,30,9,10,0,222,190,1,87,15,86,116,43,66,10018,5054,4764,3419,2839,1991,977,625,15,15761,13473,468,5706,1611,5766,7921,2727,5971],
#         '8/8/2021':['Sunday',292,7010,7302,817,1932,1594,1205,839,470,280,161,4,3987,3286,29,744,347,1033,1755,266,3157,47,78,66,35,26,13,18,8,1,165,126,1,59,9,78,96,20,30,770,1854,1528,1170,813,457,262,153,3,3822,3160,28,685,338,955,1659,246,3127],
#         '7/7/2021':['Wednesday',95,9182,9277,1060,2005,1917,1341,1217,912,499,321,5,4852,4305,120,1172,500,2067,1928,309,3301,21,24,23,12,7,3,4,0,1,62,32,1,23,2,24,27,4,15,1039,1981,1894,1329,1210,909,495,321,4,4790,4273,119,1149,498,2043,1901,305,3286],
#         '05/15/2020':['Friday',1161,5526,6687,355,1170,1171,1075,1095,895,503,413,10,3634,2914,139,1763,102,1142,851,174,2655,81,220,231,202,175,134,73,44,1,631,521,9,635,20,208,116,29,153,274,950,940,873,920,761,430,369,9,3003,2393,130,1128,82,934,735,145,2502],
#         '04/26/2020':['Sunday',443,1342,1785,94,321,336,263,287,257,125,100,2,947,830,8,377,58,356,310,44,640,13,81,58,84,76,56,35,40,0,237,206,0,169,17,93,63,16,85,81,240,278,179,211,201,90,60,2,710,624,8,208,41,263,247,28,555],
#         '05/17/2020':['Sunday',371,2150,2521,140,392,431,357,427,403,218,150,3,1310,1175,36,473,44,609,432,90,873,18,61,66,45,75,49,25,32,0,186,184,1,181,9,88,43,11,39,122,331,365,312,352,354,193,118,3,1124,991,35,292,35,521,389,79,834],
#         '6/29/2021':['Tuesday',65,8080,8145,865,1826,1723,1260,1144,793,347,187,0,4301,3738,106,939,482,1659,1516,401,3148,16,13,14,9,1,7,4,1,0,33,32,0,17,1,20,16,3,8,849,1813,1709,1251,1143,786,343,186,0,4268,3706,106,922,481,1639,1500,398,3140],
#         '3/10/2021':['Wednesday',369,14034,14403,862,4707,2794,1842,1658,1438,667,427,8,7533,6532,338,1873,802,2972,3915,671,4170,59,110,62,46,47,23,12,9,1,180,189,0,113,12,65,121,17,41,803,4597,2732,1796,1611,1415,655,418,7,7353,6343,338,1760,790,2907,3794,654,4129],
#         '6/7/2021':['Monday',112,11656,11768,1229,2539,2174,1756,1559,1311,699,487,14,6251,5428,89,1494,648,2455,2272,458,4441,20,20,14,19,18,12,7,2,0,57,55,0,32,3,42,27,1,7,1209,2519,2160,1737,1541,1299,692,485,14,6194,5373,89,1462,645,2413,2245,457,4434]
#     }
#     ordered = sorted(my_dict, key=lambda x: datetime.strptime(x, "%m/%d/%Y"))
#     print(ordered)
#     # res = list(ordered.keys())[0]
#     res = next(iter(ordered))
#     print(res)
#     print()
#     res1 = list(ordered)[-1]
#     print(res1)
# main()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

# ts = ts.cumsum()

# ts.plot()
# plt.show()

word = "word"
list_of_letters = list(word)
print(list_of_letters)
print(list_of_letters[3])

