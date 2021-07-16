"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 3:03:30
@Title : Program Aim is write a program that accepts a comma separated sequence of words as input
         and prints the unique words in sorted form (alphanumerically).
"""
from LogHandler import logger

def getUniqueWords(string1):
    """
    Description:
        This function is used for printing unique words in sorted form.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try: 
        stringList = list(string1.split(','))
        newList = []
        for counter in range(0, stringList.__len__()):
            stringList[counter] = stringList[counter].replace(' ', '')
        stringList.sort()
        for counter1 in range(stringList.__len__()):
            if newList.__contains__(stringList[counter1]):
                continue
            else:
                newList.append(stringList[counter1])
        logger.info(newList)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "red, white, black, red, green, black"
    getUniqueWords(string1)
