"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 11:13:30
@Title : Program Aim is to print only the common items.
"""
from LogHandler import logger
try:
    list1 = [1, 3, 5, 8, 9, 4]
    list2 = [0, 3, 7, 9, 2, 5]
    list3 = []
    for items in list1:
        # storing just the common elements in the list1 and list2
        if list2.__contains__(items):
            list3.append(items)
    print("Common items are :  ")
    logger.info(list3)

except Exception as e:
    logger.error(e)
