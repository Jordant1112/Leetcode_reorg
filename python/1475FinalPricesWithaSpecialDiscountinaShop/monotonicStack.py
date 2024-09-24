class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res_next = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            res_next[i]= stack[-1] if stack else 0
            stack.append(prices[i])
        res = [0] * n
        for i in range(n):
            res[i] = prices[i] - res_next[i]
        return res
