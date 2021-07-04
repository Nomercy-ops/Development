"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to generate and print dictionary .
"""
from InputValidation import Validate
from LogHandler import logger


try:
    dictionary1 ={}
    print("Enter the number")
    inputnum = Validate.getPositiveNumber()
    # storing the values in the dictionary
    for counter in range(1, inputnum):
        dictionary2 = {(counter, counter * counter) }
        dictionary1.update(dictionary2)
    logger.info(dictionary1)
except Exception as e:
    logger.error(e)
