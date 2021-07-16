"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:13:30
@Title : Program Aim is to check whether an element exists within a tuple.
"""
from LogHandler import logger

try:
    tuple1 = ('apple', 'dhoni', 'rikesh', 'ronaldinho', 'rohit')
    userInput = input("Enter the element to be searched in the tuple : ")
    # it checks if the user input is present in the tuple
    if tuple1.__contains__(userInput):
        logger.info("the string is present")
    else:
        logger.info("String not present")
except Exception as e:
    logger.error(e)
