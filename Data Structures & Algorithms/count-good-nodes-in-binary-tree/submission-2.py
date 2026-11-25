# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root:
            max_value = root.val
        else:
            return 0


        def test_nodes(root: TreeNode, curr_max) -> int:
            if root.val >= curr_max:
                curr_max2 = root.val
            else:
                curr_max2 = curr_max
            return (1 if root.val >= curr_max2 else 0) + (test_nodes(root.left,curr_max2) if root.left else 0 ) + (test_nodes(root.right,curr_max2) if root.right else 0) 
        
        return test_nodes(root,max_value)
           




