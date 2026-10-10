# Largest of Three Numbers
# Largest of Three Numbers
# Given three integers a, b, and c, find and return the largest number among them using conditional statements without relying on the built-in max() function.

# Example 1:
# Input: a = 10, b = 25, c = 15
# Output: 25

def largestOfThree(a: int, b: int, c: int) -> int:
    # Write your solution here
  large =a 
  if b>large:
    large =b

  if c>large:
    large =c
  return large    

    