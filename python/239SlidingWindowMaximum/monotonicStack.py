class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        n = len(nums)
        for i in range(n):
            start = i -k + 1
            while q and q[0] < start:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if start >= 0:
                res.append(nums[q[0]])
        return res
