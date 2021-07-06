"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 2:03:30
@Title : Program Aim is to reverse the string.
"""
from LogHandler import logger

def reverseString(string1):
    """
    Description:
        This function is used for reverse a string.
    Parameter:
        It takes string1 as a parameter.
       
    """

    try:
       
        reverse_string = string1[::-1]
        logger.info(reverse_string)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
     string1 = input("Enter the text to reverse: ")
     reverseString(string1)
