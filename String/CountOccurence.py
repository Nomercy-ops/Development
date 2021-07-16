"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 4:03:30
@Title : Program Aim is to count number of occurence in substring of string
"""
from LogHandler import logger

def countOccurence(string1):
    """
    Description:
        This function is used for count occurence of characters from the strings
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        # counting the number of occurrences of a string
        logger.info(string1.count('le'))

        #using loop
        count = 0
        strchar = 'l'
        for i in range(0,len(string1)):
            if string1[i] == strchar:
                count += 1
                continue
        print(count)
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "learn apple appleap"
    countOccurence(string1)
