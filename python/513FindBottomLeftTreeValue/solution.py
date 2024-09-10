# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        res = 0
        level = -1
        while queue:
            node, l = queue.popleft()
            if node:
                if level != l:
                    level = l
                    res = node.val
                if node.left:
                    queue.append((node.left, l+1))
                if node.right:
                    queue.append((node.right, l+1))
        return res
