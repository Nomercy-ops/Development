"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to remove items from a set if it is present.
"""

from LogHandler import logger
try:
    mySet = {1, 2, 3, 14, 15}
    item = 16
    if item in mySet:
        # element is in the list then only it'l be removed
        mySet.remove(16)
        logger.info("successfully deleted")
    else:
        # if the element is not present there it'll show as not present
        logger.info("Not present in the set")
    logger.info(mySet)

except Exception as e:
    logger.error(e)
