"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 3:03:30
@Title : Program Aim is get the last part of a string before a specified character.
"""
from LogHandler import logger

def getLastPart(string1):
    """
    Description:
        This function is used for getting last part of a string.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        character = '-'
        logger.info(string1.rsplit(character, 1)[0])
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = 'https://www.w3resource-com/python-exercises'
    getLastPart(string1)
