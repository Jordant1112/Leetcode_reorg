class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq_count = Counter(nums)
        k_pair_count = 0
        for key, val in freq_count.items():
            if k == 0:
                if val > 1:
                    k_pair_count += 1
            else:
                if (key+k) in freq_count:
                    k_pair_count += 1
        return k_pair_count
