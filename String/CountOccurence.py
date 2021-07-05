"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to count number of occurence in substring of string
"""
from LogHandler import logger

try:
    string1 = "learn apple appleap"
    # counting the number of occurrences of a string
    logger.info(string1.count('le'))
except Exception as e:
    logger.error(e)
