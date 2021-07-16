"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 9:03:30
@Title : Program Aim is to find number of occurences of element from an array.
"""
import array
from LoggerHandler import logger


def findOccurence(myArray,number):
    """
    Description:
        This function is used for finding occurences of element in array
    Parameter:
        It takes myarray and number to find its occurences
       
    """
    count  = 0
    try:
        for i in range(len(myArray)):
           if (myArray[i] == number):
                count = count+1           
        print('The Number of Occurences of', number ,'is: ' ,count,'times')

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[23,3,19,23,14,16,18,23])
        number = 23
        findOccurence(myArray,number)
    
    except Exception as e:
        logger.error(e)