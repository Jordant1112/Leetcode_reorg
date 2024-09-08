class Solution:
    def addOneRow(self, root, val, depth) -> Optional[TreeNode]:
        if not root:
            return
        if depth == 1:
            return TreeNode(val, left = root)
        self.helper(root, depth, val)
        return root
       

    def helper(self, root, remaining, val):
        if not root:
            return
        if remaining == 2:
            root.left = TreeNode(val, left = root.left)
            root.right = TreeNode(val, right = root.right)
            return
        self.helper(root, remaining-1, val)
        self.helper(root, remaining-1, val)
