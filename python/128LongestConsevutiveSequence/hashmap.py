class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            cur = 1
            down = i-1
            up = i + 1
            while down in s:
                cur += 1
                s.remove(down)
                down -= 1
            while up in s:
                cur += 1
                s.remove(up)
                up += 1
            res = max(res, cur)
        return res
