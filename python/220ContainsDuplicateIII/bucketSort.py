class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int,
            valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        d = {}
        for i, x in enumerate(nums):
            bucket = x // (valueDiff + 1)
            if bucket in seen and i - seen[bucket][0] <= indexDiff:
                return True
            if bucket -1 in seen and i - seen[bucket-1][0] <= indexDiff and
            abs(x - seen[bucket-1][1]) <= valueDiff:
                return True
            if bucket +1 in seen and i - seen[bucket+1][0] <= indexDiff and
            abs(x - seen[bucket+1][1]) <= valueDiff:
                return True
            seen[bucket] = (i, x)
        return False
