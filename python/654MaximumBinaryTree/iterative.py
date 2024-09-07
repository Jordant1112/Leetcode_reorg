class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) ->
    Optional[TreeNode]:
        stack = []
        for num in nums:
            curr = TreeNode(num)
            while stack and stack[-1] < num:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[-1] if stack else None
