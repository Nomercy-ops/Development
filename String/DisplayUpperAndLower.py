"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to takes input from the user and displays that input back in
         upper and lower cases.
"""
from LogHandler import logger

try:
    string1 = input(("Enter the string"))
    print("string in lower case ", string1.lower())
    print("string in upper case ", string1.upper())
except Exception as e:
    logger.error(e)
