# # Highest occuring element in an array
# Given an array nums of n integers, find the most frequent element in it, which is the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, return the smallest of them.

# Examples
# Example 1:

# Input:

# {"nums": [1, 2, 2, 3, 3, 3]}
# Output:

# 3
# Explanation: The number 3 appears the most (3 times). It is the most frequent element.
def highestOccurringElement(nums):
    # Write your code here

    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1
    max_freq= max(freq.values())
    return min(num for num in freq if freq[num]==max_freq)
print(highestOccurringElement([4,4,5,5,6]))