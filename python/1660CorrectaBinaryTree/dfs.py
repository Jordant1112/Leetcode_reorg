class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNOde:
        d = set()
        self.dfs(root, d)
        return root

    def dfs(self, root, d):
        if not root:
            return
        d.add(root)
        if root.right and root.right in d:
            return None
        root.right = self.helper(root.right, d)
        root.left = self.helper(root.left, d)
        return root
