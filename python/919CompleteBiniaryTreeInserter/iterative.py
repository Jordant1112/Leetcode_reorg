class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.q = self.make_queue(root) if root else deque([])
        self.root = root

    def make_queue(self, root: Optional[TreeNode]):
        q = deque([root])
        res = deque([])
        while q:
            n = len(q)
            node = q.popleft()
            if node and (not node.left or not node.right):
                self.res.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    def insert(self, val: int) -> int:
        if not self.q:
            self.root = TreeNode(val)
            self.q.append(self.root)
        else:
            curr = self.q[0]
            if not curr.left:
                curr.left = TreeNode(val)
                self.q.append(curr.left)
            elif not curr.right:
                curr.right = TreeNode(val)
                self.q.append(curr.right)
            else:
                self.q.popleft()
                return self.insert(val)
        return self.q[0].val

    def get_root(self) -> Optional[TreeNode]:
        retrun self.root
