# Even or Odd
# Given an integer n, determine whether the number is even or odd. Return "Even" if it is even, and "Odd" if it is odd.


def checkEvenOdd(n: int) -> str:
    # Write your solution here
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"    
    pass