
# Problem:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool: 
        #so it takes in s which is a string, returns a bool
        #we only want the alphanumeric characters so lets create a new string
        newS = ""
        for char in s: #go through every character in string s
            if char.isalnum(): #if its alphanumeric
                charLow = char.lower() #make that lowercase
                newS += charLow #add that lowercase to the string
        if newS == newS[::-1]: 
            #palindromes can be read the same in both ways
            #so if the string s with lowecase alphanumerics is == to its reverse
            return True
        return False #if ur here, its not a palindrome
    
# Time Complexity: O(n) because we traverse through each character in string s, memory complexity is also O(n) because we use extra memory though when we create new string s and also when we reverse it
# A solution with O(1) complexity would be to use two pointers left and right to make sure the characters stay equal till we meet in the middle