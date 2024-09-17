class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        end = False
        if not root:
            return True
        q = deque([(root)])
        
        while q:
            size = len(q)
            
            for i in range(size):
                r = q.popleft()
                if not r:
                    end = True
                else:
                    if end:
                        return False
                    q.append(r.left)
                    q.append(r.right)
        return True
