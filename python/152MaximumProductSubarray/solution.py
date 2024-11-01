class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_r = nums[0]
        max_r = nums[0]
        max_hist = nums[0]
        for i in nums[1:]:
            min_r, max_r = min(min_r*i, max_r*i, i), max(min_r *i, max_r*i, i)
            max_hist = max(max_hist, max_r)
        return max_hist
