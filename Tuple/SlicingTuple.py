"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:03:30
@Title : Program Aim is to slice a tuple.
"""
from LogHandler import logger
try:
    tuple1 = tuple(['apple', 'dhoni', 'rikesh', 'ronaldinho', 'rohit'])
    # slicing the tuple and storing in a new tuple
    tuple2 = tuple1[2:]
    logger.info(tuple2)
    tuple3 = tuple1[:3]
    logger.info(tuple3)

except Exception as e:
    logger.error(e)
