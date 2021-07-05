"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to count number of characters in a string.
"""
from LogHandler import logger

try:
    string1 = "google.com"
    # storing the characters in set as duplicates will be removed
    countedChar = {}

    for i in string1:
        if i in countedChar:
            countedChar[i] += 1
        else:
            countedChar[i] = 1
    logger.info(countedChar)

except Exception as e:
    logger.error(e)
