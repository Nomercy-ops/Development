"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to  count the number of strings where the string length is 2 or more
         and the first and last character are same from a given list of strings.
"""
from LogHandler import logger
try:
    list1 = ['abc', 'xyz', 'aba', '1221']
    # creating a new list of those elements whose length is more than 1 and the first and last element is the same
    newList = []
    for item in list1:
        if item[0]== item[-1] and item.__len__() > 1:
            newList.append(item)
            continue
    print('number of elements is ',newList.__len__() ,
          ' and the values are ', newList)

except Exception as e:
    logger.error(e)
