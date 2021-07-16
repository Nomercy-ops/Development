"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to create a frozen set. 
"""

from LogHandler import logger
try:
    set1 = {1, 2, 3, 14, 15}
    set2 = {4, 5, 6, 1, 2}

    # creating the frozen set
    set3 = frozenset({1, 2, 3, 4})
    set3 = set3 - set2
    logger.info(set3)

except Exception as e:
    logger.error(e)
