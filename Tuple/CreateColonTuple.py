"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:13:30
@Title : Program Aim is to create a colon tuple.
"""
from copy import deepcopy
from LogHandler import logger
try:
    tuple1 = tuple(['apple', 1.23, 12.019, True, 10,20])
    # copying the tuple to different tuple
    tuple2 = tuple1
    # or using deepcopy
    tuple2 = deepcopy(tuple1)
    logger.info(tuple1)
    logger.info(tuple2)

except Exception as e:
    logger.info(e)
