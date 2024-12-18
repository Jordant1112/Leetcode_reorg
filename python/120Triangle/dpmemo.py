class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.recursion(triangle, 0, 0, 0, {})


    def recursion(self, l, x, y, ans, memo):
        if x >= len(l):
            return 0
        if (x, y) in memo:
            return memo[(x,y)]
        ans += l[x][y] + min(self.recursion(l, x+1, y, ans, memo), self.recursion(l, x+1, y+1, ans, memo))
        memo[(x,y)]= ans
        return ans
            
