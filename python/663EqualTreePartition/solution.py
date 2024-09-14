class Solution:
    def checkEqualTree(self, root) -> bool:
        if not root:
            return False
        self.d = set()
        s = root.val + self.post_order(root.left) + self.post_order(root.right)
        if s % 2 != 0:
            return False
        return s // 2 in self.d

    def post_order(self, root):
        if not root:
            return 0
        l = self.post_order(root.left)
        r = self.post_order(root.right)
        self.d.add(l + r + root.val)
        return l + r + root.val
