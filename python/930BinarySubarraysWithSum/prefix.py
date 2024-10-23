class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {}
        s = 0
        res = 0
        for num in nums:
            s += num
            if s - goal in d:
                res += d[s-goal]
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        return res
