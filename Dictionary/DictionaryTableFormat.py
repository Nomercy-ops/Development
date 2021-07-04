"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to print dictionary values in table format.
"""
from LogHandler import logger
try:
    myDictionary = {'1': 1}
    string = 'w3resource'
    for counter in string:
        myDictionary[counter] = string.count(counter)
        # printing the key and values as tables
    for (key, vals) in myDictionary.items():
        print(key, " \t", vals)
except Exception as e:
    print(e)
