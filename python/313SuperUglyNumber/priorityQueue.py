class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        pq = []
        for prime in primes:
            heapq.heappush(pq, (1, prime, 1))
        ugly = [0] * (n+1)
        p = 1
        while p <= n:
            val, prime, idx = heapq.heappop(pq)
            if val != ugly[p-1]:
                ugly[p-1] = val
                p += 1
            heapq.heappush(pq, (ugly[idx] * prime, prime, idx + 1))
        return ugly[n]
