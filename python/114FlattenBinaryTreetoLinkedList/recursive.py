class Solution:
    def flatten(self, root:Optiona[TreeNode]) -> None:
        if not root:
            return None
        self.res = []
        self.preorder(root)
        node = self.res.pop(0)
        for n in self.res:
            node.right = n
            node.left = None
            node = n
        return root
    
    def preorder(self, root):
        if not root:
            return
        self.res.append(root)
        self.preorder(root.left)
        self.preorder(root.right)
