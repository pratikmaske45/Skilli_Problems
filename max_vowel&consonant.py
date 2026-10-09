# Find Most Frequent Vowel and Consonant
# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency. Find the consonant (all other letters excluding vowels) with the maximum frequency. Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.


class solution:
    def maxfreqsum(self, s:str) -> int:
        vowel = "aeiou"
        max_vowel = 0
        max_consonant =0

        for char in s:
            frequency = s.count(char)
            if char in vowel:
                max_vowel = max(max_vowel, frequency)
            else:
                max_consonant= max(max_consonant, frequency)
        return max_vowel + max_consonant
obj = solution()
print(obj.maxfreqsum("successes"))

