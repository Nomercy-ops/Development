"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 2:03:30
@Title : Program Aim is to to get a string from a given string where all occurrences of its
         first char have been changed to '$', except the first char itself.
"""
from LogHandler import logger
def getStringOccurence(string1):
    """
    Description:
        This function is used for getting string first char as $.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        string2 = string1[1:string1.__len__()]
        for counter1 in range(1, string1.__len__()):
            if string1[counter1] == string1[0]:
                string1 = string1[0] + string2.replace(string1[counter1], '$')
        logger.info(string1)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "restart"
    getStringOccurence(string1)

