"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:03:30
@Title : Program Aim is to reverse a tuple.
"""
from LogHandler import logger
try:
    tuple1 = tuple(['apple', 'dhoni', 'rikesh', 'ronaldinho', 'rohit'])
    # reversing the tuple and storing the output as a tuple in the variable
    tuple2 = tuple(reversed(tuple1))
    logger.info(tuple2)

except Exception as e:
    logger.error(e)
