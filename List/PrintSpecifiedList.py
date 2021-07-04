"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 10:03:30
@Title : Program Aim is print a specified list after removing the 0th, 4th and 5th elements.
"""
from LogHandler import logger
try:
    myList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    # count stores the number of the elements deleted
    count = 0
    myList.__delitem__(0 - count)
    # as 1 element deleted increment the value of count
    count += 1
    logger.info(myList)
    myList.__delitem__(4 - count)
    count += 1
    logger.info(myList)
    myList.__delitem__(5 - count)
    count += 1
    logger.info(myList)

except Exception as e:
    logger.info(e)
