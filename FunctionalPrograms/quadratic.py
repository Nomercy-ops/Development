"""
@Author: Rikesh Chhetri
@Date: 2021-06-27 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-27 14:33:30
@Title : Program Aim is find the roots of the equation a*x*x + b*x + c. 
"""

import math

def quadratic():
    """
    Description:
        This function is used for calculating  root of a equation .
        It takes point a ,b and y values from the user and then find delta by applying formulae.
        And then calculate the root of the equation.
          
    """

    try:
        a = int(input("Enter value for a : "))
        b = int(input("Enter value for b : "))
        c = int(input("Enter value for c : "))

        delta = abs(b * b - 4 * a * c) # getting absolute value.

        root1 = (-b + math.pow(delta, 1 / 2)) / (2 * a)
        root2 = (-b - math.pow(delta, 1 / 2)) / (2 * a)
        print("The First Root Of Equation Is " , root1)
        print("The Second Root Of Equation Is ", root2)
    
    except ValueError:
        print("Enter a Numeric value")
        quadratic()
    except ZeroDivisionError:
        print("Value of a shouldnt be zero :")
        quadratic()

quadratic()