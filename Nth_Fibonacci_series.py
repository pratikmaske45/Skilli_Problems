# Nth Fibonacci Series
# Given a non-negative integer n, return the nth number in the Fibonacci sequence.

# Constraints 0 <= n <= 30

# The sequence is: Index: 0 1 2 3 4 5 6 7 8 9 Value: 0 1 1 2 3 5 8 13 21 34

# Examples:- Input: 5 Output: 5

# Input: 8 Output: 21

# Input: 7 Output: 13

# Input: 0 Output: 0

def fibonacci(n:int)-> int:
    if n < 0 or n>30:
        return False
    
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a
  
