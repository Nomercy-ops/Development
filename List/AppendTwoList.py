"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 10:03:30
@Title : Program aim is to append the two different list.
"""
from LogHandler import logger
try:
    list1 = ['Red', 'green', 'deer', 'pikachu', 'nomercy', 'lottery']
    list2 = ['troy', 'Rohan', 'Laptop']
    for string in list2:
        # appending each word from list2 into list1
        list1.append(string)
    logger.info(list1)

except Exception as e:
    logger.error(e)
