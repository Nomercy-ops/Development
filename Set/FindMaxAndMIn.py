"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to find maximum and minimum in a set. 
"""

from LogHandler import logger
try:
    set1 = {1, 2, 3, 4, 5, 5, 6, 7, -1, -3}
    logger.info(set1)
    # printing the min value in the set
    logger.info(min(set1))
    # printing the max value in the set
    logger.info(max(set1))

except Exception as e:
    logger.error(e)
