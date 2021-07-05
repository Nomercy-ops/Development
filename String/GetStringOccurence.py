"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to to get a string from a given string where all occurrences of its
         first char have been changed to '$', except the first char itself.
"""
from LogHandler import logger
try:
    string1 = "restart"
    string2 = string1[1:string1.__len__()]
    for counter1 in range(1, string1.__len__()):
        if string1[counter1] == string1[0]:
            string1 = string1[0] + string2.replace(string1[counter1], '$')
    logger.info(string1)

except Exception as e:
    logger.error(e)
