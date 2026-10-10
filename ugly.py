# Ugly Number
# An ugly number is a positive integer whose prime factors are only 2, 3, and 5.

# Given an integer n, determine whether n is an ugly number.

# To check this, repeatedly divide n by 2, 3, and 5 as long as it is completely divisible by them. After removing all possible factors:

# If the remaining value is 1, then n is an ugly number. If the remaining value is greater than 1, then n has another prime factor and is not an ugly number. Any n <= 0 is not an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i

        return n == 1

