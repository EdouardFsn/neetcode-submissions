# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue =  deque()
        if root:
            queue.append(root)
        last_seen = root
        
        while queue:
            length = len(queue)
            for i in range(length):
                last_seen = queue.popleft()
                if last_seen.left:
                    queue.append(last_seen.left)
                if last_seen.right:
                    queue.append(last_seen.right)
            output.append(last_seen.val)
        return output

        