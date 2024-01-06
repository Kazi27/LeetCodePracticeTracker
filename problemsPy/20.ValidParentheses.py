
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #initialize stack, push is .append(stuff), pop is .pop()
        
        #hashmap = {'{' : '}', '(' : ')', '[' : ']'} #make ur keyvalue pairs
        hashmap = {')' : '(', ']' : '[', '}' : '{'}

        for x in s:
            if x in hashmap: #checks if x is ) or ] or } aka a key
                if stack and stack[-1] == hashmap[x]:
                #stack[-1] is top of stack, hashmap[x] gives val at that key
                #so if key is ) it cheks if at key ) do u have value (
                #if they match pop
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(x)
        
        #if not stack == False: #is stack empty
        if len(stack) == 0:
            return True #if it is then valid parenthesis
        
# Time Complexity:
# O(n) because we are going through each input character once, memory/space complexity is also  O(n) because stack could be of size n
