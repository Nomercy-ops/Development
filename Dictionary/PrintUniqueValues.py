"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to get unique values from dictionary.
"""

from LogHandler import logger
    
try:
    myDictionary = {"IV": "S001", "VII": "S002", "VI": "S001", "IIV": "S005", "IIIV": "S005", "V": "S009", "VIII": "S007"}

    print("Printing the set created from sets")
    # storing as set as sets do not store duplicate elements
    newList = set(myDictionary.values())
    for counter in newList:
        print("Unique Values : ",counter)
     
except Exception as e:
   logger.error(e)
