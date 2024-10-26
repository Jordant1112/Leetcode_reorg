# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res =[]
        q = deque()
        q.append(root)
        result = -1
        while q:
            size = len(q)
            tmp = 0
            for _ in range(size):
                node = q.popleft()
                tmp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(res, -tmp)
        if len(res) < k:
            return -1
        while k:
            result = -heapq.heappop(res)
            k -= 1
        return result if result != -1 else -1 
