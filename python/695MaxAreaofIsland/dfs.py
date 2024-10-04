class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0
                    self.count_island(grid, i, j)
                    self.res = max(self.count, self.res)
        return self.res
    
    def count_island(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 
        if grid[i][j] == 0:
            return 
        self.count += 1
        grid[i][j] = 0
        self.count_island(grid, i+1, j)
        self.count_island(grid, i-1, j)
        self.count_island(grid, i, j + 1)
        self.count_island(grid, i, j - 1)

