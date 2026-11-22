# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        output = []

        while queue:
            length = len(queue)
            levelx = []
            for i in range(length):
                popped = queue.popleft()
                if popped != None:
                    levelx.append(popped.val)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
            output.append(levelx)
        return output
        