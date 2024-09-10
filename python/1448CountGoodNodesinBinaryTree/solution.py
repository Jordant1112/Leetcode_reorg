class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.traverse(root, root.val)
        return self.res

    def traverse(self, root, pathMax):
        if not root:
            return
        if pathMax <= root.val:
            self.res += 1
        pathMax = max(pathMax, root.val)
        self.traverse(root.left, pathMax)
        self.traverse(root.right, pathMax)


