# Replace a Character
# Given a string, a character oldChar, and a character newChar, replace every occurrence of oldChar with newChar.

# All other characters should remain unchanged.

# Examples Example 1 Input: String = "banana" oldChar = 'a' newChar = 'x'

# Output: "bxnxnx"

# Example 2 Input: String = "hello" oldChar = 'l' newChar = 'p'

# Output: "heppo"

# Example 3 Input: String = "programming" oldChar = 'm' newChar = 'x'

# Output: "prograxxing"

# Output Format return the modified string.

class Solution:
    def replacechar(self, s, oldchar,newchar):

        result =""
        for char in s:
            if char == oldchar:
                result += newchar
            else:
                result += char
        return result
obj =Solution()
print(obj.replacechar("banana","a","x"))     
print(obj.replacechar("hello","l", "p"))       


