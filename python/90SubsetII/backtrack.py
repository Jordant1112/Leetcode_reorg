class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        output = []
        for i in range(len(nums)+1):
            self.backtrack(nums, output, i, 0)
        return self.res

    def backtrack(self, nums, output, idx, start):
        if len(output) == start:
            self.res.append(output)
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums, output+[nums[i]], i+1, start)
