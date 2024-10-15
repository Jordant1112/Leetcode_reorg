# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        if root.left:
            self.left(root.left, res)
        if root.left or root.right:
            self.leaf(root, res)
        if root.right:
            self.right(root.right, res)
        return res
    
    def left(self, root, res):
        if not root:
            return
        if root.left:
            res.append(root.val)
            self.left(root.left, res)
        elif root.right:
            res.append(root.val)
            self.left(root.right, res)
        return res
    
    def right(self, root, res):
        if not root:
            return
        if root.right:
            self.right(root.right, res)
            res.append(root.val)
            
        elif root.left:
            self.right(root.left, res)
            res.append(root.val)
        return res
    
    def leaf(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
        self.leaf(root.left, res)
        self.leaf(root.right, res)
        return res
