"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to get a sorted list of a ascending order.
"""
from LogHandler import logger
try:
    myList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    # sorting the variables according to the second element in each tuple of list
    
    for counter1 in range(0, list1.__len__() - 1):
        for counter2 in range(counter1 + 1, myList.__len__()):
            if list1[counter1][0] > myList[counter2][1]:
                temp = myList[counter1]
                myList[counter1] = myList[counter2]
                myList[counter2] = temp

    logger.info(myList)
except Exception as e:
    logger.error(e)
