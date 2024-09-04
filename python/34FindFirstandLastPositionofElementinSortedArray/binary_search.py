class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1,-1]
        l = self.left_bound(nums,target)
        r = self.right_bound(nums, target)


    def left_bound(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m -1
        return l

    def right_bound(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m -1
        return r
