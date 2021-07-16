"""
@Author: Rikesh Chhetri
@Date: 2021-06-27 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-27 16:33:30
@Title : Program Aim is find the triplet number when added gives zero. 
"""

def findTriplets(arr, n):
    """
    Description:
        This function is used for finding Triplets when added give zero.

    Parameter:
        It takes two parrameter arr is a array list of elements and,
        n here is the length of the array.

    """

    found = False   # Boolean Expression
    # Looping in to the array elements till (n-2) element for the 'i' th element
    for i in range(0, n - 2):
        # Looping in to the array from the (i+1)th elements position till  penultimate
        for j in range(i + 1, n - 1):
            # Taking the jth elements position till the last elements position
            for k in range(j + 1, n):
                # Checking the sum of ith jth and kth  to be Zero
                if (arr[i] + arr[j] + arr[k]) == 0:
                    found = True
                    # Returning the elements If a+b+c = 0
                    return (arr[i], arr[j], arr[k])

    if not found:
        d = "Triplets not found try with another elements "
        return d

if __name__ == "__main__":
    try:
        # Taking the input from the user to find the length of the array
        number_of_elements = int(input("Enter the Number of elements:\n"))
        arr = []  # creating a list to store the elements
        print("\nEnter the elements:")
        for i in range(number_of_elements):  # Looping for the N number of elements
            # Taking the user input and storing it to the array list
            arr.append(int(input()))
        # calling the function to find the triplets
        print(findTriplets(arr, number_of_elements))

    except ValueError:
        print("Enter a valid integer value as input")
