
# Problem:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    from typing import List
    from typing import Optional
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: #list1 and 2 are pointers pointing to nodes in the list
        dummy = ListNode() #this is ur final linked list
        tail = dummy #this points to the default node in the final linked list

        while (list1 and list2) != None: #as long as both lists exist
            if list1.val < list2.val: #if list1 val is < list2 val
                tail.next = list1 #the pointer of tail now points to list1 node
                list1 = list1.next #advance list1 pointer to next node
            else:
                tail.next = list2 #the pointer of tail now points to list2 node
                list2 = list2.next #advance list2 pointer to next node
            tail = tail.next #advance tail pointer to next node
        
        if list1 == None: #if u exhaust list1
            tail.next = list2 #take the rest of the nodes from list 2

        elif list2 == None: #if u exhaust list2
            tail.next = list1 #take the rest of the nodes from list 1

        return dummy.next #dummy is the dumb first one so we dont want that, so we do dummy.next to get the rest of it except the first one 
    
# Time Complexity:
# O(n) because you are traversing both lists at the same time, space is O(1) because no extra memory is needed, you're just using pointers