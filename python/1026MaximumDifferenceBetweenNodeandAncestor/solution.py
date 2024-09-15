class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return [float('inf'), float('-inf')]
        l = self.helper(root.left)
        r = self.helper(root.right)
        minVal = min(minVal, l[0], r[0])
        maxVal = max(maxVal, l[1], r[1])
        self.res = max(self.res, root.val - minVal, maxVal - root.val)
        return [minVal, maxVal]
