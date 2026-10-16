# Mean or average of array
# Given an integer array arr of size n, calculate the mean (average) of all the elements in the array and return its floor value.

# The mean is calculated by dividing the sum of all array elements by the total number of elements.

# The floor value is the greatest integer less than or equal to the calculated mean.

# Examples:
# Example 1:-
# Input: arr = [1, 3, 4, 2, 6, 5, 8, 7]
# Output: 4
# Explanation:
# Sum of elements = 36
# Number of elements = 8
# Mean = 36 / 8 = 4.5
# Floor value = 4


def mean(arr):
    sum = 0
    for num in arr:
        sum += num
        avg = sum // len(arr)
    return avg
print("The average of given array is:",mean([1,3,4,2,6,5,8,7]))    

