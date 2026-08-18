# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p.val == root.val or q.val == root.val:
        #     return root
        
        # say we start at 5, if given 3 and 7, we know it must be 5 since 3 < 5 < 7
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if given 3, 4 we know it has to be a node in the left
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)   
        else:
            return root