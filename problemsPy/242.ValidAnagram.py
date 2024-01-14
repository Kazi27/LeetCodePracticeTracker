
# Problem:
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: True

# Example 2:
# Input: s = "rat", t = "car"
# Output: False

# Solution:
# This solution is in python3
class Solution(object):
    def isAnagram(self, s, t):
        newS = sorted(s)
        newT = sorted(t)
        if newT == newS:
            return True
        return False
        """Below is solution in outdated python, does the same thing as above
        :type s: str
        :type t: str
        :rtype: bool
        
        if len(s) == len(t):  # Base condition, all anagrams will have the same length
            sorted_s = sorted(s)
            sorted_t = sorted(t)  # Sort both strings; all anagrams, when sorted, will result in equivalent strings

            if sorted_s == sorted_t:
                return True  # Strings match after sorting

        return False  # If you reach here, s and t are not anagrams
        """

# Complexities:
# The time complexity for sorting is O(n log n), and then you're sorting both strings so O(n log n) twice which generalizes to O(n log n)
# The space complexity is O(1) because sorting is done in place and we use the same amount of memory regardless of the size of s or t