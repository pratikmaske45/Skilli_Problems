# #Valid Anagram
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 &lt;= len(s), len(t) &lt;= 5 * 10^4
# s and t consist of lowercase English letters.

def is_anagram(s:str, t:str)-> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False

    for value in count.values():
        if value != 0:
            return False
                            
    return True
print(is_anagram("anagram", "nagaram")) 
print(is_anagram( "car", "rat"))