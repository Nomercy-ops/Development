"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 8:03:30
@Title : Program Aim is to find a repeated items in a tuple.
"""
from LogHandler import logger
try:
    tuple1 = ('apple', 1.23, 12.019, 'f', 10, 20, 'apple', 20)
    tuple2 = []
    count = 0
    for counter in range(tuple1.__len__()):
        count = 0
        for counter2 in range(counter + 1, tuple1.__len__()):
            # tuple 2 will store  the values if it is duplicated in the tuple1 and  was not in tuple2
            if tuple1[counter] == tuple1[counter2] and (tuple2.__contains__(tuple1[counter2])) is False:
                tuple2.append(tuple1[counter2])
    logger.info(" the elements having the duplicates are ", tuple2)

except Exception as e:
    logger.error(e)
