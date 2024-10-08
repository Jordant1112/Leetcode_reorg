class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m+1] < nums[m] and nums[m-1] < nums[m]:
                return m
            if nums[m+1] > nums[m]:
                l = m + 1
            else:
                r = m
        return l
