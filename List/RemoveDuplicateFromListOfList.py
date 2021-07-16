"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 12:13:30
@Title : Program Aim is Remove duplicates from list of list.
"""
from LogHandler import logger
try:
    list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    list1.sort()
    list2 = []
    # iterate through each element in the list
    for item in list1:
        if item not in (list2):
            list2.append(item)
        continue
    logger.info(list2)

except Exception as e:
    logger.error(e)
