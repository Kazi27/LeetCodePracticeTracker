
# Problem:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    from typing import List
    from typing import Optional
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #so .next is the arrow aka the pointer, we initialize prev, curr, next
        #pointers so we don't lost track, nodes are lost when 0 pointers are 
        #pointing to them. Okay so we want to traverse through the entire thing
        prev = None #initially previous is null
        curr = head #current is at head
        while (curr != None): 
            #as long as current is not null (at the end curr will be null)
            next = curr.next #save the node next to curr
            curr.next = prev #arrow reversal, currs next is now what was b4 curr
            prev = curr #move prev up, prev is one behing curr always
            curr = next #move curr up cause remember u save curr.next each iterat
        return prev #at the end, head of ur new reversed list is prev
    
# Complexities:
# Time complexity would be O(n) because we are traversing through the whole list with next prev and curr
# Memory complexity is O(1) because no data structures like stack or something, we are just manipulating pointers         