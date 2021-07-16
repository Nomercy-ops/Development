"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to convert list to nested dictionary.
"""
from LogHandler import logger
try:
    myDictionary = {}
    id = ['emp1', 'emp2', 'emp3']
    empInfo = [{'name': 'Bob', 'job': 'Mgr'},
               {'name': 'Kim', 'job': 'Dev'},
               {'name': 'Sam', 'job': 'Dev'}]

    for item in id:
        for info in empInfo:
            myDictionary[item] = info
    logger.info(myDictionary)
except Exception as e:
    logger.info(e)
