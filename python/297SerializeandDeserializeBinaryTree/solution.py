class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root: TreeNode):
        return self.post_order(root)

    def post_order(self, root):
        if not root:
            return '#'
        left = self.post_order(root.left)
        right = self.post_order(root.right)
        subTree = left + ',' + right + ',' + str(root.val)
        return subTree

    def deserialize(self, data):
        if not data:
            return []
        d = data.split(',')
        return self.helper(d)

    def helper(self, d):
        if not d:
            return
        r = d.pop()
        if r == '#':
            return None
        root = TreeNode(int(r))
        root.right = self.helper(d)
        root.left = self.helper(d)
        return root
