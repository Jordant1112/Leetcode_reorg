class Solution:
    def frequencySort(self, s: str) -> str:
        chartoFreq = {}
        for c in s:
            chartoFreq[c] = chartoFreq.get(c, 0) + 1
        res = []
        while pq:
            freq, c, heapq.heappop(pq)
            res.append(-freq*c)
        return ''.join(res)

