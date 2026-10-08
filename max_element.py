# Maximum Element
# Given a non-empty list of integers nums, find and return the maximum value in the
#  list without using the built-in max() function.

def max_element(nums: list[int]) -> int:
    max =nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
print("the max element in nums is:",max_element([1,5,3,9,2]))        
