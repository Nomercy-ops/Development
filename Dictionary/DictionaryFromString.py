"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is Track the count of the letters from the string..
"""
from LogHandler import logger

try:
    # creating an empty dictionary
    myDictionary = dict()
    string = 'w3resource'
    # storing the values in the dictionary along with their count
    for counter in string:
        myDictionary[counter] = string.count(counter)
    logger.info(myDictionary)

except Exception as e:
    logger.error(e)
