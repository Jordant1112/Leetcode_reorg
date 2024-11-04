class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = 0
        max_val = max(nums)
        min_val = min(nums)
        buckets = []
        B = defaultdict(list)
        n = len(nums)
        avg = (max_val - min_val) / (n-1)
        for num in nums:
            if num == max_val:
                idx = n-1
            else:
                idx = (num - min_val) // avg
            B[idx].append(num)

        for i in range(len(n)):
            if i in B:
                buckets.append((min(B[i]), max(B[i])))
        for i in range(1, len(buckets)):
            res = max(res, abs(buckets[i-1][-1] - buckets[i][0]))
        return res

