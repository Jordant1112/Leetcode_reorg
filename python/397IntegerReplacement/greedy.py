class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.dp(n)

    def dp(self, n):
        if n == 1:
            return 0
        if n < 1:
            return float('inf')
        if n % 2 == 0:
            return 1 + self.dp(n/2)
        else:
            minus = 1 + self.dp(n-1)
            plus = 1 + self.dp(n+1)
            return min(plus, minus)
