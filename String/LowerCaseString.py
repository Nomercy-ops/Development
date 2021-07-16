"""
@Author: Rikesh Chhetri
@Date: 2021-07-05
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 2:33:30
@Title : Program Aim is to lowercase first n characters in a string.
"""
import InputValidation as validate
from LogHandler import logger

def getLowerCase(string1):
    """
    Description:
        This function is used for getting first n characters into lowercase string.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        print("Enter the value of n")
        # taking a number input from user
        num_input = validate.getPositiveNumber()
        if num_input < string1.__len__():
            # storing the 2 parts of string lowering first part and rest part as it is
            string1 = string1[:num_input].lower() + string1[num_input:]
            logger.info(string1)
        else:
            logger.info("The number is more than the size of the string")
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "ASWATHAMA"
    getLowerCase(string1)
