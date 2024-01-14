
# Problem:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    from typing import List
    from typing import Optional
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head #start at the head pointer
        fast = head

        while fast != None and fast.next != None: #as long as the fast pointer isnt at null or the next node isnt null
            slow = slow.next #increment slow by 1
            fast = fast.next #increment fast twice so by 2
            fast = fast.next
            if slow == fast: #if they do meet then u have a cycle
                return True
        return False #u do not have a cycle
    
# Complexities:
# Time complexity is O(n) because you have to traverse all n nodes
# For space complexity, in this optimal soultion we use two pointers no data structs so we don't use extra memory so memory is O(1) 
# If we used a hashmap memory complexity would be O(n) because potentially every node would be on the hashmap, the way you'd do this is
# youd have every visited node in the hashmap and then in one of the checks you do you're gonna check if the node thats next is already in the hashmap
# if it is you have a cycle. Hashmap data struct and the fact that potentially all nodes will be there means memory complexity would be O(n) with time complexity being O(n) because we traverse all n nodes