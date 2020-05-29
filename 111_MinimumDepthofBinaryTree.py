# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None or root.right is None:
            if root.left:
                return self.minDepth(root.left) + 1
            else:
                return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1