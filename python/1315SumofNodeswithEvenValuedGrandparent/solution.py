# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, None, None)
        return self.res
    


    def dfs(self, root, parent, grandparent):
        if not root:
            return
        if grandparent and grandparent.val % 2 == 0:
            self.res += root.val
        self.dfs(root.left, root, parent)
        self.dfs(root.right, root, parent)
