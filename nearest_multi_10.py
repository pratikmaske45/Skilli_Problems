# Nearest multiple of 10
# You are given a string s representing a positive integer. Your task is to round the number to the nearest multiple of 10. If the number is equally distant from two multiples of 10, return the smaller multiple. Return the rounded number as a string.

# Example 1 Input: s = "29" Output: "30" Explanation: The nearest multiples of 10 are 20 and 30. Since 29 is closer to 30, the answer is 30.

# Example 2 Input: s = "15" Output: "10" Explanation: The number 15 is equally distant from 10 and 20. Since we choose the smaller multiple in a tie, the answer is 10.

# Constraints 1 <= s.length <= 10^5 s contains digits from '0' to '9' s represents a positive integer

# Examples
# Example 1:
# Input: {"s":"29"}
# Output: 30


def multi(s):
    num = int(s)
    remainder = num % 10
    if remainder <= 5:
        ans = num - remainder
    else: 
        ans = num + (10- remainder)
    return ans 
print("Nearest multiple of 10:",multi(29))