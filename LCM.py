# Lowest Common Multiple (LCM) of Two Numbers
# You are given two integers n1 and n2. Your task is to find the Lowest Common Multiple (LCM) of the two given numbers. The LCM of two integers is the smallest positive integer that is divisible by both integers.

# Examples
# Example 1:
# Input:
# n1 = 4, n2 = 6
# Output:
# 12
def findLcm(n1, n2):
    # Write your code here
    gcd =0 
    for i in range(1, min(n1,n2)+1):
        if n1 % i ==0 and n2 % i ==0:
            gcd = i
            lcm = n1*n2//gcd
    return lcm     