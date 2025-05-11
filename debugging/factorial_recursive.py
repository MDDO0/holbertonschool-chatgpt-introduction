#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input number from the command line argument,
# calculate its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
