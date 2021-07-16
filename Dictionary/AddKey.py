"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to add a key into dictionary.
"""


try:
    from InputValidation import Validate
    from LogHandler import logger
except ImportError as e:
    print(e)
except Exception as e:
    print(e)

def addKey():
    """
    Description:
        This method is used for adding key into Dictionary

    """
    try:
        myDictionary = {"0": 16, "1": 11, "2": 23}
        print("The dictionary before sorting is")
        # printing the dictionary
        for key in myDictionary:
            print("For key ", key, " value is: ", myDictionary[key])
        # taking user input
        print("Enter the key to be added")
        inputkey = Validate.getInteger()
        print("Enter the value to be added")
        inputvalue = Validate.getInteger()
        # adding the input to the dictionary
        myDictionary[inputkey.__str__()] = inputvalue
        logger.info(myDictionary)
    except Exception as e:
        logger.info(e)
            
addKey()       
