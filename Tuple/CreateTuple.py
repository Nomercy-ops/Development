"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:03:30
@Title : Program Aim is to create a tuple.
"""
from LogHandler import logger
try:
    # creating a tuple
    tuple1 = tuple({'apple', 'banana'})
    logger.info(tuple1)

except Exception as e:
    logger.error(e)
