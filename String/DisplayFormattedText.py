"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-06 1:03:30
@Title : Program Aim is to display formatted text (width=50) as output.
"""
from LogHandler import logger

def displayFormattedText(string1):
    """
    Description:
        This function is used for getting formatted string.
    Parameter:
        It takes string1 as a parameter.
       
    """
    try:
        # formatting the string and then printing it
        print("{}={}".format(string1, 50))
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    string1 = "width"
    displayFormattedText(string1)
