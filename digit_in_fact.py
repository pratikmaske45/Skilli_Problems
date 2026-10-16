# No. of digits in a factorial 
# Given a positive integer n, find the number of digits in the value of n! (factorial of n).

# The factorial of a number n is the product of all positive integers from 1 to n.

# n! = 1 * 2 * 3 * 4 * 5 *.......*n

# Return the total number of digits in the factorial value.

# Example:
# Example 1:-
# Input: n = 5
# Output: 3
# Explanation: Factorial of 5 is: 5 * 4 * 3 * 2 * 1

# The number 120 contains 3 digits.

def fact(n):
    fact = 1
    count = 0
    for i in range(1,n+1):
        fact *= i
    while fact > 0:
        digit = fact % 10
        count += 1
        fact = fact//10
    return count        
print("The number of digits in factorial is",fact(5))

