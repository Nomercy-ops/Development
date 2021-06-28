"""
@Author: Rikesh Chhetri
@Date: 2021-06-27 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-27 14:03:30
@Title : Program Aim is to take  x and y as integer input and calculate distance using Euclidean formulae. 
"""

import math

def get_distance():

    """
    Description:
        This function is used for calculating distance using Euclidean formulae.
        It takes point x and y values from the user and then calculate. 
          
    """
    try:
        x = int(input("Enter the X Co-ordinate:"))  # X Co-ordinate
        y = int(input("Enter the Y Co-ordinate:"))  # Y Co-ordinate
        distance = math.sqrt((x * x + y * y))       # Applying the distance formula of Euclidean
        print(" The Euclidean Distance from origin ",'x'," and ",'y'," is ",distance,"")

    except ValueError:
        print("Enter a Valid Interger value")
        get_distance()

get_distance()
