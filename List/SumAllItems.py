"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to summ all items on a list.
"""
from LogHandler import logger
try:
    # initialising the list
    list1 = [1, 2, 3, 4, 5]
    # variable to store the addition of the values in the list
    total = 0
    for elements in list1:
        # adding the values of the list
        total += elements
    logger.info(total)
    #by sum method 
    logger.info(sum(list1))
except Exception as e:
    logger.error(e)
