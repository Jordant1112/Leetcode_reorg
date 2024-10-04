class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        dirs = [[0, 1], [0, -1], [-1,0], [1, 0]]
        for i in range(length):
            if grid[i][0] == 1:
                self.filledges(grid, i, 0)
            if grid[i][width-1] == 1:
                self.filledges(grid, i, width-1)
        for j in range(width):
            if grid[0][j] == 1:
                self.filledges(grid, 0, j)
            if grid[length-1][j] == 1:
                self.filledges(grid, length-1, j)
        res = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    res += 1
        return res


    def filledges(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.filledges(grid, i-1, j)
            self.filledges(grid, i+1, j)
            self.filledges(grid, i, j+1)
            self.filledges(grid, i, j-1)
        
