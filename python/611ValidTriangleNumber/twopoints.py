class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums)-1
        ans = 0
        while k > 0:
            i = 0
            j = k-1
            while j > i:
                if nums[j] + nums[i] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
            k -=1
        return ans
