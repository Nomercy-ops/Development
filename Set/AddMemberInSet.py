"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to add items in a set.
"""

from LogHandler import logger
try:
    mySet = {1, 2, 3}
    logger.info(mySet)
    # adding the new element in the set
    mySet.add(12)
    mySet.add(13)
    logger.info(mySet)
except Exception as e:
    logger.error(e)
