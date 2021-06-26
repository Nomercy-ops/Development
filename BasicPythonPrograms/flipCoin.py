"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 12:03:30
@Title : Program Aim is to flip a coin with userinput N times and print the head and tails percentage. 
"""

import random


def flipCoin(userinput):
    """flipCoin [This method is used for fliping of coin by using random if number is 0 then it will be added to head count, 
                and in case of number 1 tails keep increament untill for loops ends]
    Args:
        userinput ([int]): [This args is used for getting number of flips that user wants.]
    """
    # variables for storing and tracking count of heads and tails
    heads = 0
    tails = 0
    headspercent = 0
    tailspercent = 0

    if userinput > 0:
        count = 0
        for count in range(count, userinput):
            coin = random.randint(0, 1)

            if coin == 0:
                heads += 1
            else:
                tails += 1

            headspercent = ((heads / (heads + tails)) * 100)
            tailspercent = ((tails / (heads + tails)) * 100)

        print("Heads percentage is : " + str(headspercent))
        print("Tails percentage is : " + str(tailspercent))

    else:
        print("Enter a Positive Number : ")

userinput = int(input("\n How many times do you want to flip a coin :  "))
flipCoin(userinput)
print(flipCoin.__doc__)
