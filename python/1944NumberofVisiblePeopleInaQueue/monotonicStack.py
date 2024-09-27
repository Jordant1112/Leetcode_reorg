class Solution:
    def canSeePersonCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0] * n
        for i in range(n-1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            res[i] = count + 1 if stack else count
            stack.append(heights[i])
        return res