# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.res = set()
        self.traverse(root)
        

    def find(self, target: int) -> bool:
        return True if target in self.res else False
        
    def traverse(self, root):
        if not root:
            return
        self.res.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.traverse(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.traverse(root.right)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
