"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program aim is to get the difference between the two lists.
"""
from LogHandler import logger

try:
    list1 = ['Red', 'yop', 'der', 'poy', 'op', 'edr']
    list2 = ['pop', 'poy', 'Red']
    list3 = []
    for string1 in list1:
        if list2.__contains__(string1):
            continue
        else:
            # storing the elements which are in list1 but not in list2
            list3.append(string1)
    print("difference of two list is: ")
    logger.info(list3)

except Exception as e:
    logger.error(e)
