class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        output = []
        nums.sort()
        self.backtrack(nums, res, output)
        return res

    def backtrack(self, nums, res, output):
        if not nums:
            res.append(output)
            return 
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            self.backtrack(nums[:i]+nums[i+1:], res, output + [nums[i]])

