"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 11:23:30
@Title : Program Aim is to split a list based on first character of word
"""
from LogHandler import logger
try:
    list1 = ['Panasonic', 'Rog', 'Orients', 'Gamma', 'Rage',
             'Agression', 'Mind', 'Matuer', 'Ethincity', 'Rise']
    # creating the list of just the first character in each item of the list
    list2 = [item[0] for item in list1]
    logger.info(list2)

except Exception as e:
    logger.info(e)
