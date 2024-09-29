class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        numToFreq = {}
        res = []
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        for num, freq in numToFreq.items():
            bucket[freq].append(num)
        for b in range(len(bucket)-1, -1, -1):
            if bucket[b] != []:
                while k and len(bucket[b]) > 0:
                    res.append(bucket[b].pop())
                    k -= 1
        return res

