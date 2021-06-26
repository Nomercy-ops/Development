"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 12:33:30
@Title : Program Aim is to Computes the prime factorization of N using brute force. 
"""


def prime_fact(number):
    """

    prime_fact 
        This function used while loop for Traversing till i*i <= N and and while traversing it will check
        in if conditions that number mod i is true then it will increament i value and continue for loop 
        and returns our number.

    Parameter:
        number  is used for getting user number so that number goes through while loop for finding prime.

    Return:
        prime factor of number values as a output.

    """
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number


userinput = int(input("Enter an Number:"))
print(" Prime Factors : " + str(prime_fact(userinput)))
