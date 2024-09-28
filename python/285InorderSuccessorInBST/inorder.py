class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.res = []
        self.inorder(root)
        pvalue = p.val
        pre_seen = float('inf')
        print(self.res)
        for val in self.res:
            if val > p.val and val < pre_seen:
                pre_seen = val
        if pre_seen == float('inf'):
            return None
        return TreeNode(pre_seen)


    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
