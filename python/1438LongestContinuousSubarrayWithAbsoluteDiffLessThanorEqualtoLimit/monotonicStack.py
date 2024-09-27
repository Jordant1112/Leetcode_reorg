class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        incq = deque()
        decq = deque()
        res = 0
        while right < len(nums):
            while incq and incq[-1] > nums[right]:
                incq.pop()
            incq.append(nums[right])

            while decq and decq[-1] < nums[right]:
                decq.pop()
            decq.append(nums[right])

            while decq[0] - incq[0]  > limit:
                if decq[0] == nums[left]:
                    decq.popleft()
                if incq[0] == nums[left]:
                    incq.popleft()

                left += 1
            res = max(res, right - left + 1)
            right += 1
        return right
