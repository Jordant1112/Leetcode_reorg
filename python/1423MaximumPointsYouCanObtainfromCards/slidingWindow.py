class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        val = sum(cardPoints)
        n = len(cardPoints)
        if k == n:
            return val
        tmp = sum(cardPoints[:n-k])
        res = 0
        res = max(res, val - tmp)
        for i in range(n-k, n):
            tmp += cardPoints[i]
            tmp -= cardPoints[i - (n-k)]
            res = max(res, val-tmp)
        return res
