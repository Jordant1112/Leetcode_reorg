class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [[0,-1], [0, 1], [-1, 0], [1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j, dirs)
        return res
    
    def dfs(self, grid, i, j, dirs):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for dir in dirs:
            self.dfs(grid, i + dir[0], j + dir[1], dirs)
        

