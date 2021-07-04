"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to create intersection of sets.
"""

from LogHandler import logger

try:
    set1 = {1, 2, 3, 14, 15}
    set2 = {4, 5, 6, 1, 2}
    # storing the elements which are in both the sets
    set3 = set1.intersection(set2)  
    logger.info(set3)

except Exception as e:
    logger.error(e)
