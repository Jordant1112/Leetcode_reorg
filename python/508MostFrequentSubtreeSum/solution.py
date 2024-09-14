# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.res = {}
        self.post_order(root)
        res = []
        max_count = max(self.res.values(), default = 0)
        for key, val in self.res.items():
            if val == max_count:
                res.append(key)
        return res

    def post_order(self, root):
        if not root:
            return 0
        l = self.post_order(root.left)
        r = self.post_order(root.right)
        tmp = l + r + root.val
        self.res[tmp] = self.res.get(tmp, 0) + 1
        return tmp
