
# Problem:
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    from typing import List
    from typing import Optional
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: #if the node you're at does not exist
            return None 
        
        temp = root.left 
        root.left = root.right
        root.right = temp #this is a basic swapping of the nodes

        self.invertTree(root.left) #recursive call on the root of the left subtree
        self.invertTree(root.right) #recursive call on the root of the left subtree
        return root #now the whole tree is inverted
    
# Time Complexity:
# O(n) because we are traversing all n nodes in each recursive call
# O(h) is the memory complexity because we are feeding in the root of each subtree each recursive call, if tree is balanced its O(log n) tho but worst case its a linked list or skewed