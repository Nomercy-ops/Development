"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to create a set.
"""

from LogHandler import logger
try:
    # creating the new set
    mySet = {1, 2, 3}
    logger.info(mySet)

except Exception as e:
    logger.error(e)
