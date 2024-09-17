class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        maxWidth = 0
        while q:
            size = len(q)
            start = 0
            end = 0
            for i in range(size):
                cur, cur_id = q.popleft()
                if i == 0:
                    start = cur_id
                if i == size -1:
                    end = cur_id
                if cur.left:
                    q.append((cur.left, cur_id * 2))
                if cur.right:
                    q.append((cur.right, cur_id * 2 + 1))
            maxWidth = max(maxWidth, end - start + 1)
        return maxWidth
