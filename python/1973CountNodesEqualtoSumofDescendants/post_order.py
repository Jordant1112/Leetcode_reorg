# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.post_order(root)
        return self.res


    def post_order(self, root):
        if not root:
            return 0
        l = self.post_order(root.left)
        r = self.post_order(root.right)
        if l + r == root.val:
            self.res += 1
        return l + r + root.val

