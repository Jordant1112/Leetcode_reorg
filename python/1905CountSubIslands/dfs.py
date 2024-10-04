class Solution:
    cdef countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)
        res = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    res += 1
                    self.dfs(grid2,i,j)
        return res



    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
