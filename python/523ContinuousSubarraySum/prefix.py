class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = nums[0]
        s = set()
        s.add(0)
        for i in range(1, len(nums)):
            new = prefix + nums[i]
            if new % k in s:
                return True
            s.add(prefix % k)
            prefix = new
        return False
