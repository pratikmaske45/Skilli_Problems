# Sum from 1 to N
# Sum from 1 to N
# Given a positive integer n, calculate and return the sum of all integers from 1 up to n inclusive using a loop or arithmetic formula.

# Example 1:
# Input: n = 5
# Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15.

def sumUpToN(n: int) -> int:
    # Write your solution here
    sum =0
    for i in range(n+1):
        sum = sum +i
    return sum    
     

    pass