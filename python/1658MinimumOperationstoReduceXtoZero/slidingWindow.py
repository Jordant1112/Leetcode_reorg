class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        target = s - x
        i = j = 0
        max_len = curr_sum = 0
        found = False
        for j in range(len(nums)):
            curr_sum += nums[j]
            while i <= j and curr_sum > target:
                curr_sum -= nums[i]
                i += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, j - i + 1)
        return len(nums) - max_len if found else -1
