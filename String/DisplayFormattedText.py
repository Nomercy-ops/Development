"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 1:03:30
@Title : Program Aim is to display formatted text (width=50) as output.
"""
from LogHandler import logger

try:
    string1 = "width"
    # formatting the string and then printing it
    print("{}={}".format(string1, 50))
except Exception as e:
    logger.error(e)
