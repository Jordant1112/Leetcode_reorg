class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = []
        d = set()
        q.append((root, None))
        for node, parent in q:
            if node.right and node.right.val in d:
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None
                return root
            d.add(node.val)
            if node.right:
                q.append((node.right, node))
            if node.left:
                q.append((node.left, node))

