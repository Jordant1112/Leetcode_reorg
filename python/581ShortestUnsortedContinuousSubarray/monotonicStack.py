class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = float('inf')
        right = float('-inf')
        res = 0
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for i in range(n-1, -1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        if left == float('inf') or right == float('-inf'):
            return 0
        return right - left + 1
