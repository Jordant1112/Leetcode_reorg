class Solution:
    def __init__(self):
        self.node_to_copy = {}

    def copyRandomBinaryTree(self, root: 'Optional[Node]') ->
    'Optional[NodeCopy]':
        if not root:
            return None
        if root in self.node_to_copy:
            return self.node_to_copy[root]
        r = NodeCopy(root.val)
        self.node_to_copy[root]=r
        r.random = self.copyRandomBinaryTree(root.random)
        r.left = self.copyRandomBinaryTree(root.left)
        r.right = self.copyRandomBinaryTree(root.right)
        return r
