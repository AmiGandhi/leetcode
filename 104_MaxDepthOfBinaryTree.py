# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        
        currNodeList = [root] if root else []
        depth = 0
        while currNodeList and len(currNodeList)>0:
            queue = []
            depth += 1
            for elem in currNodeList:
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            currNodeList = queue
        return depth