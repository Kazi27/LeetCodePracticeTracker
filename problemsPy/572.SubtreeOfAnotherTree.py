
# Problem:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #if the subtree is null, null is a subtree of all trees so return true
            return True

        if not root: #if the tree is null itself, it can't have subtrees so return false
            return False

        z = self.isSameTree(root, subRoot) #if they are the same tree, subroot is a subtree of the root so return true
        if z:
            return True

        a = self.isSubtree(root.left, subRoot) #recursive call checking if subroot is a subtree of the left or right subtree of root
        b = self.isSubtree(root.right, subRoot)
        if a or b:
            return True

        return False #if ur here, none of the if statements executed so false
        
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: #if both trees are null, they are the same
            return True
        
        if not root or not subRoot: #if one of the trees are null but the other isnt, they are not the same
            return False
        
        if root.val == subRoot.val: #so if ur here, both trees exist, and if the values match then
            x = self.isSameTree(root.left, subRoot.left) #check values of their left and right children
            y = self.isSameTree(root.right, subRoot.right) #do this recursively for all nodes
            if x and y: #if their children values also match return true
                return True
        
        return False #if ur here the trees exist but values do not match so return false