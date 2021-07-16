"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to iterate over items of a set.
"""

from LogHandler import logger
try:
    # creating a new set
    myset = {1, 2, 3}
    # iterating through the elements in the set
    for item in myset:
        logger.info(item)

except Exception as e:
    logger.error(e)
