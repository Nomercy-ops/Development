"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to find the permutations of a list.
"""
from LogHandler import logger
import itertools

try:
    # initializing the list
    list1 = [1, 2, 3]
    permutationObjects = itertools.permutations(list1)
    finalPermutation = list(permutationObjects)
    logger.info(finalPermutation)

except Exception as e:
    logger.error(e)
