"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to reverse the string.
"""
from LogHandler import logger

try:
    string1 = input("Enter the text to reverse: ")
    # using slice 
    start = stop = None # setting start and  stop as none
    step = -1           # -1 last index  of string
    reverse_slice = slice(start, stop, step)
    logger.info(string1[reverse_slice])
  
except Exception as e:
    logger.error(e)
