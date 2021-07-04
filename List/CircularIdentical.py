"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 11:03:30
@Title : Program Aim is to find that if a list is circularly identical or not.
"""
from LogHandler import logger
try:
    list1 = ['10', '10', '0', '0', '10']
    list2 = ['10', '10', '10', '0', '0']
    list3 = list1 * 2
    
    # traversal in list1 
    for counter1 in range(0, len(list1)):
        count = 0   
    # check if list2 == list1 circularly 
        for counter2 in range(counter1, counter1+ len(list1)):
            if list2[count]== list3[counter2]:
                count += 1
            else:
                break
           # if all n elements are same circularly 
    if count == len(list1):
        logger.info("list is circularly identical")
    else:  
        logger.info("list is not circularly identical")      

except Exception as e:
    logger.error(e)
   
