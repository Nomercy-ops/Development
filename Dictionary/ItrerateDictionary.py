"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to iterate over dictionary values..
"""

from LogHandler import logger
try:
        myDictionary = {'0': 11, 1: 13,'3':16,'4':23}
       
        for item in myDictionary.items():
            logger.info(item)
        print("printing using keys")

        for key in myDictionary:
            print("Key: ", key, " values:", myDictionary[key])
        
        print("printing key value pairs")
        for (key, value) in myDictionary.items():
            print("Key: ", key, " values:", value)

except Exception as e:
    logger(e)
        