class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        self.memo = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))
        return res

    def dfs(self, matrix, i, j):
        res = 1
        m = len(matrix)
        n = len(matrix[0])
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            if x < 0 or y < 0 or x >= m or y >= n:
                continue
            if matrix[x][y] > matrix[i][j]:
                res = max(res, self.dfs(matrix,x,y) + 1)
        self.memo[i][j] = res
        return res

