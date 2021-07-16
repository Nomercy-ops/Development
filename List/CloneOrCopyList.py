"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to clone or copy the list.
"""
from LogHandler import logger
try:
    list1 = [2, 5, 8, 7, 4, 9, 3, 1]
    
    list2 = []
    # cloning the list 1 and storing it in the list1
    list2 = list1.copy()
    logger.info("List1 value is : ")
    logger.info(list1)
    logger.info("copy of List1 value is : ")
    logger.info(list2)
except Exception as e:
    logger.info(e)
