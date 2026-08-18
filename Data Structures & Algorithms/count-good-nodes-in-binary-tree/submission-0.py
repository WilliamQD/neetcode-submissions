# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)

    
    def dfs(self, node, maxNum):
        if not node:
            return 0
        count = 0 
        if node.val >= maxNum:
            maxNum = node.val
            count += 1

        return count + self.dfs(node.left, maxNum) + self.dfs(node.right, maxNum)