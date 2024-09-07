class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.helper(root.left, root.right)
        return root

    def helper(self, root1, root2):
        if not root1 or not root2:
            return
        root1.next = root2
        if root1.left and root1.right:
            self.helper(root1.left, root1.right)
        if root1.right and root2.left:
            self.helper(root1.right, root2.left)
        if root2.left and root2.right:
            self.helper(root2.left, root2.right)

