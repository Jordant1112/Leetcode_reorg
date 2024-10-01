class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        self.backtrack(nums, res, tmp)
        return res

    def backtrack(self, nums, res, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], res, tmp + [nums[i]])

