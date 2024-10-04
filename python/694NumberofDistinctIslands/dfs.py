class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sb = []
                    self.dfs(grid, i, j, sb, 0)
                    islands.add(''.join(str(sb)))
        return len(islands)
    
    def dfs(self, grid, i, j, sb, dir):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        sb.append(dir)
        sb.append(',')
        self.dfs(grid, i-1,j, sb, 1)
        self.dfs(grid, i+1,j, sb, 2)
        self.dfs(grid, i,j-1, sb, 3)
        self.dfs(grid, i,j+1, sb, 4)
        sb.append(-dir)
        sb.append(',')
