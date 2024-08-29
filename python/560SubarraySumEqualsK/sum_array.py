class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res = 0
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i] 
            if tmp - k in d:
                res += d[tmp-k]
            if tmp not in d:
                d[tmp] = 1
            else:
                d[tmp] += 1
        return res
