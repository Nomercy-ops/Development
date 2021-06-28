"""
@Author: Rikesh Chhetri
@Date: 2021-06-27 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-27 12:03:30
@Title : Program Aim is to take input from the user and print 2D array. 
"""

def two_dimensional_array():
    """
    Description:
        This function is used for printing 2D array. 
        It takes number of rows and colums and,
        also element of array from user.    
    """

    try:

        row = int(input("Enter the number of rows:"))
        col = int(input("Enter the number of columns:"))

        # for storing 2D array of type list
        matrix = []
        print("Enter the entries row wise:")

        for i in range(row):  # loop for row
            array = []
            for j in range(col):  # loop for column
              array.append(int(input()))   # inserting input into blank array
            matrix.append(array)  # appending array with matrix

        # for loop for printing the 2D array
        print("The 2D array is given below:")
        for i in range(row):
            for j in range(col):
                print(matrix[i][j], end="  ")
            print()

    except ValueError:
        print("Enter a valid integer input")
        two_dimensional_array()

two_dimensional_array()
