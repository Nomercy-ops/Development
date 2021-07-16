"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:13:30
@Title : Program Aim is to convert list into tuple.
"""
from LogHandler import logger
try:
    list1 = ['apple', 'dhoni', 'rikesh', 'ronaldinho', 'rohit']
    # copying the list as tuple in new variable
    tuple1 = tuple(list1)
    logger.info(tuple1)

except Exception as e:
    logger.info(e)
