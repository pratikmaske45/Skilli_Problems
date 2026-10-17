 # sum of arithmetic series
# An arithmetic series is a sequence of numbers in which the difference between consecutive terms remains constant. This difference is called the common difference.
# You are given three integers n, a, and d, where a represents the first term of the series, d represents the common difference, and n represents the total number of terms.

# The arithmetic series is defined as:
# a, a + d, a + 2d, a + 3d, ...
# Calculate and return the sum of the first n terms of the arithmetic series.

# Example: Example 1:-
# Input: n = 5, a = 1, d = 3 Output: 35
# Explanation:
# The first five terms are 1, 4, 7, 10, 13. Their sum is 1 + 4 + 7 + 10 + 13 = 35.


def arithmetic(a,d,n):
    sum = 0
    for i in range(1,n+1):
        ans = a + (d*(i-1))
        sum += ans
    return sum     
print("The sum of arithmetic is:",arithmetic(1,3,5))
