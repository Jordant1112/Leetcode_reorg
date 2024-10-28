class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for j in range(n-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                res = max(res, j - stack.pop())
        return res
