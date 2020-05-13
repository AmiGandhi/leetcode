# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        
        currNodeList = [root] if root else []
        ans = []
        root = [root.val] if root else []
        while currNodeList and len(currNodeList)>0:
            queue =[]
            for node in currNodeList:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            currNodeList = queue
            level = [leaf.val for leaf in queue]
            if len(level)>0:
                ans.append(level)
        ans.reverse()
        if len(root)>0:
            ans.append(root)
        return ans
            