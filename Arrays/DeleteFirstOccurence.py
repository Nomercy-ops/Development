"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 9:03:30
@Title : Program Aim is to remove first occurence of element from array
"""
import array
from LoggerHandler import logger


def deleteOccurence(myArray,number):
    """
    Description:
        This function is used for finding occurences of element in array
    Parameter:
        It takes myarray and number to find its occurences
       
    """
    
    try:
        for i in range(len(myArray)):
           if (myArray[i] == number):
                myArray.remove(number)
                break           
        print("Array after removing",number,'is' , myArray)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[23,3,19,23,14,16,18,23])
        number = 23
        deleteOccurence(myArray,number)
    
    except Exception as e:
        logger.error(e)