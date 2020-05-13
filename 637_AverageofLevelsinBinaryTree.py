# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        
        currNodeList = [root] if root else []
        avg_list = [root.val] if root else []
        
        while currNodeList and len(currNodeList)>0:
            queue=[]
            for node in currNodeList:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes_list = [nodes.val for nodes in queue]
            total=0
            for n in nodes_list:
                total += n
            if len(nodes_list)>0:
                avg = total/len(nodes_list)
                avg_list.append(avg)
            currNodeList = queue
        return avg_list