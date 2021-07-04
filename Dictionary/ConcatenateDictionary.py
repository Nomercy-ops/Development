"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to concatenate dictonary.
"""
from LogHandler import logger

def concatDictionary():
    try:
        
        newdictionary = {'': ''}

        dict1 = {0: 11, 1: 13}
        dict2 = {2: 12, 3: 16}
        dict3 = {4: 14, 5: 17}
    
        # copy dict1 to new dictionary
        newdictionary = dict1.copy()

        # updating the dictionary if keys not present then gets added
        newdictionary.update(dict2)
        newdictionary.update(dict3)

        for key in newdictionary:
            print("key: ", key, " value: ", newdictionary[key])
    
    except Exception as e:
        logger.error(e)

concatDictionary()