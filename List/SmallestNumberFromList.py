"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to find smallest number from a list.
"""
from LogHandler import logger

try:
        list1 = [1, 2, 3, 4, -1, 5]
        # printing the min value in the list using the min function
        print("Smallest element is : ")
        logger.info(min(list1))
except Exception as e:
        logger.error(e)
