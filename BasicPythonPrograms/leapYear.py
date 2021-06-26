"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 12:20:31
@Title : Program Aim is check the given user input of year is a leap year or not.. 
"""


def check_leapyear(year):
    """

    Description: 
        This function will first check that a give user input is 4-digit or not,if that is true then
        It will further check for condition if  statement and gives the result.

    Parameter:
        year  is used for getting user input of year for checking leap year or not.

    """

    if (year <= 999 or year > 9999):
        year = int(input("please enter a 4 - digit number : "))
    else:

        if (year % 400 == 0 & year % 100 != 0) or (year % 4 == 0):

            print(year, " is a leap year ")
        else:
            print(year,  " is not a leap year ")


year = int(input("Enter the Year : "))
check_leapyear(year)
