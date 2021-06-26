"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 12:11:30
@Title : Program Aim is to Print the Nth harmonic number: 1/1 + 1/2 + ... + 1/N .
"""


def harmonic_generate(N):
    """harmonic_generate [This function will generate harmonic values of a series by aplyying formulae inside for loop.]

    Args:
        N ([int]): [The args N is used for getting user input of int number ]

    Returns:
        [harmonic]: [returns value of harmonic number by using harmonic formulae]
    """
    # taking initial harmonic value as 1.00
    harmonic = 1.00

    # loop to apply the formula
    for i in range(2, N + 1):
        harmonic += 1 / i
    return harmonic


userinput = int(input("Enter the Number : "))
if userinput != 0:
    print("The Nth harmonic of '", userinput, "' is '",
          round(harmonic_generate(userinput), 2), "'.")
else:
    print("Enter the Number other than '0'")
