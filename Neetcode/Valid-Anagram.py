# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
    # Input: s = "racecar", t = "carrace"
    # Output: true

# Example 2:
    # Input: s = "jar", t = "jam"
    # Output: false

# I used a Hash Map method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): # check if s and t are the same size
            return False

        countS, countT = {},{} #Hash Map

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # makes sure key exist on the hashmap, count the character at position i
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False 
        return True