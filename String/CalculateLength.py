"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to calculate length of the string.
"""
from LogHandler import logger
try:
    string1 = "rikeshchauhan"
    # printing the value of the string and the length of the string
    print("String is ", string1, " and length of the string is", len(string1))
except Exception as e:
    logger.error(e)
