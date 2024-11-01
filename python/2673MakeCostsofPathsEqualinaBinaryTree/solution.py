class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n-1, -1, -1):
            if i * 2 + 2 >= n:
                continue
            l = cost[i*2+1]
            r = cost[i*2+2]
            ans += max(l, r) - min(l, r)
            cost[i] += max(l, r)
        return ans
