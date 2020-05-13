# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        
        currNodeList = [root] if root else []
        ans = [[root.val]] if root else []
        while currNodeList and len(currNodeList)>0:
            queue = []
            for node in currNodeList:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = [leaf.val for leaf in queue]
            if len(level)>0:
                ans.append(level)
            currNodeList = queue
        return ans