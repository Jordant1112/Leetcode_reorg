class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        stack = [root]
        res = ''
        visited = set()
        while stack:
            curr = stack[-1]
            if curr in visited:
                stack.pop()
                res += ')'
            else:
                visited.add(curr)
                res += f'(str(curr.val)'
                if not curr.left and curr.right:
                    res += '()'
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return res[1:-1]
