"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:03:30
@Title : Program Aim is to unpack tuple in several variables.
"""
from LogHandler import logger
try:
    tuple1 = tuple(['apple', 23,  5.20, False])
    # unpacking the values in different variables
    tupleString, tupleInt, tupleFloat, tupleBoolean = tuple1
    # printing each of the variables taken from tuple
    logger.info(tupleString)
    logger.info(tupleInt)
    logger.info(tupleFloat)
    logger.info(tupleBoolean)

except Exception as e:
    logger.error(e)
