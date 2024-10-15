class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) ->
    Optional[TreeNode]:
        if not root or not root.right and not root.left:
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newRoot
