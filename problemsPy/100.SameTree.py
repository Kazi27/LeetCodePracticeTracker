
# Problem:
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#  Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #p means exists, not p means dne, if both p and q dne, theyre equal so return True
            return True
        
        if not p or not q or p.val != q.val: #if p OR q dne like one exists but the other does not, return false. If a val doesnt match the other one, return false
            return False

        
        x = self.isSameTree(p.right, q.right) #cheks if the right subtrees match
        y = self.isSameTree(p.left, q.left) #same as above
        if x and y == True: #if x and y are true, theyre the same tree
            return True
        return False  