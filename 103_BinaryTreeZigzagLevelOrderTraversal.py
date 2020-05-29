# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        currNodeList = [root] if root else []
        ans = [[root.val]] if root else []
        
        while currNodeList and len(currNodeList)>0:
            queue = []
            
            for elem in currNodeList:
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                
            level = [node.val for node in queue]
            if level and len(level)>0:
                i = len(ans)
                if i%2==0:
                    ans.append(level)
                else:
                    level.reverse()
                    ans.append(level)
            currNodeList = queue
        return ans
                