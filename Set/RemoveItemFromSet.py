"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to remove items from a set.
"""

from LogHandler import logger
try:
    mySet = {1, 2, 3, 12, 13, 14}
    logger.info(mySet)
    # remove the element from the list
    mySet.remove(12)
    mySet.remove(14)
    logger.info(mySet)

except Exception as e:
    logger.error(e)
