# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Flag = True
        
        def dfs(node):
            if node is None:
                return (0, True)
            
            left_ht, left_bal = dfs(node.left)
            right_ht, right_bal = dfs(node.right)

            height = max(left_ht, right_ht) + 1
            if abs(left_ht - right_ht) > 1:
                curr_bal = False
            else:
                curr_bal = True
            bal = left_bal and right_bal and curr_bal

            return (height, bal)
        
        
        return dfs(root)[1]

            