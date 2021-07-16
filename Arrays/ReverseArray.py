"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 9:03:30
@Title : Program Aim is to reverse the elements of array.
"""
import array
from LoggerHandler import logger


def reverseArray(myArray):
    """
    Description:
        This function is used for displaying Reverse array.
    Parameter:
        It takes my to reverse the array items.
       
    """
    try:
        logger.info("Original array: ")
        logger.info(myArray)
        myArray.reverse()
        logger.info("Reverse order of Array items:")
        logger.info(myArray)
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[23,13,19,37,14,16,18])
        reverseArray(myArray)
    
    except Exception as e:
        logger.error(e)