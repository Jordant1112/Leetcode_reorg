class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) ->
    Optional[TreeNode]:
        if not root:
            return None
        res = None
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if node.val == u.val and queue:
                    res, next_level = queue.popleft():
                        if next_level == level:
                            return res
                        return None
                    if node.left:
                        queue.append((node.left, level+1))
                    if node.right:
                        queue.append((node.right, level+1))
        return res
