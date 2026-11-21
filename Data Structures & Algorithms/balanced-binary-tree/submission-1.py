# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.truth = True

        def dfs (curr) -> int:
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.truth = self.truth and (1 >= (max(left,right) - min(right,left)))        
            return 1 + max (left,right)
        dfs(root)
        return self.truth

        