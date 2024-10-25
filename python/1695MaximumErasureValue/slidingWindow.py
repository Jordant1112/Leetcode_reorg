class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = {}
        i = total = res = 0
        n = len(nums)
        for j in range(n):
            total += nums[j]
            if nums[j] not in d:
                d[nums[j]] = 1
            else:
                d[nums[j]] += 1
            while i < j and d[nums[j]] > 1:
                d[nums[i]] -= 1
                total -= nums[i]
                i += 1
            res = max(res, total)
        return res
