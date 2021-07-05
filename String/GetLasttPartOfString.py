"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 3:03:30
@Title : Program Aim is get the last part of a string before a specified character.
"""
from LogHandler import logger
try:
    string1 = 'https://www.w3resource-com/python-exercises'
    logger.info(string1.rsplit('-', 1)[0])
except Exception as e:
    logger.error(e)
