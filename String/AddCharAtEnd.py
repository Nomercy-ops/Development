"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 3:03:30
@Title : Program Aim is to o add 'ing' at the end of a given string length should be at least 3
"""
from LogHandler import logger

def addCharacterAtEnd(string1):
    """
    Description:
        This function is used for adding character at the end of the string
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        if string1.__len__() < 3:
            logger.info("string length should be more then 3")
        else:
            if string1.endswith("ing"):
                # if already has ing
                string1 += 'ly'
            else:
                string1 += 'ing'
            logger.info(string1)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = input("Enter a string : ")
    addCharacterAtEnd(string1)
