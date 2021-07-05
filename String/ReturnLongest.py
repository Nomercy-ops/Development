"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 9:03:30
@Title : Program Aim is to take a list of words and returns the length of the longest one.
"""
from LogHandler import logger
from InputValidation import Validate
try:
    list1 = []
    print("Enter the number of entries : ")
    num_input = Validate.getPositiveNumber()
    for counter in range(0, num_input):
        list1.append(input("Enter the string : "))
        longestLength = 0
        longString = ""
        for item in list1:
            if item.__len__() > longestLength:
                # if length greater than current store the length
                longestLength = item.__len__()
                longString = item
        print("longest element is ", longString)

except Exception as e:
    logger.info(e)
