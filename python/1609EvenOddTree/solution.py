class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root, 0)])
        flag = True
        while q:
            size = len(q)
            res = None
            for i in range(size):
                node, level = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 != 1 or (res and res >= node.val):
                        return False
                else:
                    if node.val % 2 != 0 or (res and res <= node.val):
                        return False
                res = node.val
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
        return True
