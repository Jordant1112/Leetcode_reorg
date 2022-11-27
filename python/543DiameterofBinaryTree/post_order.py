class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.diameter_check(root)
        return self.res

    def diameter_check(self, root):
        if not root:
            return 0
        l = self.diameter_check(root.left)
        r = self.diameter_check(root.right)
        self.res = max(self.res, l+r)
        return 1 + max(l,r)
