"""
@Author: Rikesh Chhetri
@Date: 2021-06-29 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-29 12:03:30
@Title : Program Aim is to generate distinct coupon numbers.. 
"""

import random

def distinct_coupons(userInput):
    """

    Description:
        This function is used for  generate distinct coupon numbers.

    Parameter:
        userinput is used for getting number of coupons user want to generate

    """

    try:
        array = []  # empty array is used for storing data
        for i in range(userInput):
            generated_number = random.randint(0,userInput)
            array.append(generated_number)
    
        # only selecting unique numbers using set.
        unique = set(array)
        print("The Distinct coupons are : ", list(unique))
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        userInput = int(input("Enter Total Numbers to generate coupons: : "))
        distinct_coupons(userInput)

    except ValueError:
        print("enter a valid integer input")
