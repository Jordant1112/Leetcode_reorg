class Solution:
    def addOneRow(self, root, val, depth) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if level == depth-1:
                tmp_left = node.left
                tmp_right = node.right
                node.left = TreeNode(val, left = node.left)
                node.right = TreeNode(val, right = node.right)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return root
