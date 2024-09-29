class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        res = []
        pq = []
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        for num, freq in numToFreq.items():
            heapq.heappush(pq, (-freq, num))
        while k:
            freq, num = heapq.heappop(pq)
            res.append(num)
            k -= 1
        return res
