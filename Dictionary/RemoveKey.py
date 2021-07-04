"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to delete key from  dictonary.
"""
from InputValidation import Validate
from LogHandler import logger


try:
    myDictionary = {'0': 11, 1: 13,'3':16,'4':23}
    print("Enter the key to be deleted")
    number = Validate.getInteger()
    # deleting the element from the dictionary
    try:
        myDictionary.__delitem__(number)
        if len(myDictionary) > 0:
            logger.info(myDictionary)
        else:
            logger.error("dictionary empty")
    except KeyError:
        logger.error('Key not found')
        
except Exception as e:
    logger.error(e)
