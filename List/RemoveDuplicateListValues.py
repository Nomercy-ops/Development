"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to  remove duplicate values from a list.
"""
from LogHandler import logger
try:
    list1 = [2, 5, 1, 2, 4, 4, 2, 3, 2, 1]
    list2 = []
    for element in list1:
        if list2.__contains__(element):
            continue
        else:
            # storing the elements in the list which have not yet encountered
            list2.append(element)
    print(" List after removing duplicate values are : ")
    logger.info(list2)
except Exception as e:
    logger.error(e)
