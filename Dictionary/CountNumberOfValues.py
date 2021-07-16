"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to count number of values that is of list.
"""
from LogHandler import logger
try:

    myDictionary = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }
    count = 0
    # for key, value in dictionary items
    for (key, value) in myDictionary.items():
        if isinstance (value,list):
            count += len(value)
    logger.info(count)

except Exception as e:
    logger.info(e)
