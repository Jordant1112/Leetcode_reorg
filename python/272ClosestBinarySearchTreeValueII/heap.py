class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        tmp = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                heapq.heappush(tmp, (abs(node.val-target), node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        for i in range(k):
            s, val = heapq.heappop(tmp)
            res.append(val)
        return res
