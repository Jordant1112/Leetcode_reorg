# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque()
        q.append([root, 0])
        while q:
            size = len(q)
            if q[-1][1] % 2 != 0:
                tmp_size = size / 2
                for i in range(int(tmp_size)):
                    q[i][0].val, q[size-i-1][0].val = q[size-i-1][0].val, q[i][0].val
            for j in range(size):
                r, level = q.popleft()
                if r.left:
                    q.append([r.left, level+1])
                if r.right:
                    q.append([r.right, level+1])
        return root
