class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        if root.left and not root.right:
            return f'{root.val}({l})'
        if root.right and not root.left:
            return f'{root.val}()({r})'
        return f'{root.val}({l})({r})'
