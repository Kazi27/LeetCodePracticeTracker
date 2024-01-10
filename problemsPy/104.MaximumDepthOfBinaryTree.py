
# Problem:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: #base case, when the node does not exist
            return 0
        
        leftD = self.maxDepth(root.left) #get the depth of the left subtree till the point ur at at a leaf and root = none in the next iteration
        rightD = self.maxDepth(root.right) #same as above
        return max(leftD, rightD) + 1 #get the max of both subtrees and add one for the node you're currently at