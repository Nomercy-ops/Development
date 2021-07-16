"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to clear a set. 
"""

from LogHandler import logger
try:
    set1 = {1, 2, 3, 14, 15}
    set1.clear()
    logger.info(set1)

except Exception as exep:
    logger.error("Process stopped because %s" % exep)
