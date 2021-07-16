"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to find the list of words that are longer than n from a given list of words.
"""
from InputValidation import Validate
from LogHandler import logger

try:
    list1 = ['Prayas', 'Deepak', 'Sunil', 'Veejay', 'Suhas', 'Narayan', 'Ajay']
    print("Enter the length ")
    length = Validate.getPositiveNumber()
    # iterating through the list
    for string in list1:
        # printing only those whose length is more than length specified by user
        if string.__len__() > length:
            logger.info(string)
        else:
            logger.info("sorry didnt find string in a list with these length")

except Exception as e:
    logger.error(e)
