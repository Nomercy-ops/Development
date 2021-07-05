"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:13:30
@Title : Program Aim is to remove item from a tuple
"""
from LogHandler import logger
try:
    tuple1 = tuple(['apple', 'dhoni', 'rikesh', 'ronaldinho', 'rohit'])
    print("Enter the item to be removed")
    userInput = input()
    # as tuple is immutable storing the values of tuple in the list
    list1 = list(tuple1)
    # removing the element from the list
    try:
        list1.remove(userInput)
        logger.info("successfully deleted")
    except Exception as e:
        logger.error("not found")
    # storing values back to the tuple from the updated list
    tuple1 = tuple(list1)
    logger.info(tuple1)

except Exception as e:
    logger.error(e)
