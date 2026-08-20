# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {val: i for i, val in enumerate(inorder)}
        # preorder tells us 1 is root, 2/3/4 could all be left
        # inorder tells us 2 is left and 3/4 are right given 1 is root
        
        self.pre_idx = 0
        
        # 1. Nest the helper function inside buildTree (remove 'self' from its parameters)
        def dfs(l, r):
            if l > r:
                return None
            
            # This is now 100% legal Python because dfs is inside buildTree, 
            # so it has direct access to the 'preorder' parameter!
            root_val = preorder[self.pre_idx] # same as doing preorder[0] except we dont need to slice preorder everytime
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            root_idx = self.inorder_map[root_val]
            
            # 2. Call the nested function directly without 'self.'
            root.left = dfs(l, root_idx - 1)
            root.right = dfs(root_idx + 1, r)
            
            return root
            
        # 3. Return the initial call directly
        return dfs(0, len(inorder) - 1)
