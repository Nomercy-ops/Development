"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 9:03:30
@Title : Program Aim is to display array elements with index values.
"""

import array
from LoggerHandler import logger


def displayArray(myArray):
    """
    Description:
        This method is used for displaying array items using indel value.
    Parameter:
        Myarray to itreate amd get the array items.
       
    """
    try:
        # getting items of array using for loop
        for i in range(len(myArray)):
            logger.info(myArray[i])

       #without for loop
        logger.info(myArray[0])
        logger.info(myArray[1])
        logger.info(myArray[2])
        logger.info(myArray[3])
        logger.info(myArray[4])
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[23,13,19,37,14])
        displayArray(myArray)
    
    except Exception as e:
        logger.error(e)