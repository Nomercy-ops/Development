"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 12:11:30
@Title : Program Aim is to print the power of two of if 0 <= N < 31 .
"""


def power_table(input):
    """

    Description:
        This function is used for printing power of 2 where by taking for loop we will iterate our loop
        that times and input is the number of times user want to iterate but it is capped to 31. 

    Parameter:
        input is used for getting user input and it is getting N values.

    """
    for i in range(input):
        if i <= input:
            final = 2 ** i
    print("2 *", i, " = ", (final))


userinput = int(input("Enter the number : "))
if(userinput >= 0 & userinput <= 31):
    power_table(userinput)
else:
    print("Please Enter Valid Input ")
