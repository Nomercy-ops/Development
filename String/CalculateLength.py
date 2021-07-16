"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 3:03:30
@Title : Program Aim is to calculate length of the string.
"""
from LogHandler import logger
def calculateLength(string1):
    """
    Description:
        This function is used for calculating the length of a string.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        # printing the value of the string and the length of the string
        print("String is ", string1, " and length of the string is", len(string1))
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "rikeshchauhan"
    calculateLength(string1)
