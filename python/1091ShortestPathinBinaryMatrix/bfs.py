class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        dirs = [[1,0],[1,1], [0,1], [0,-1], [-1, 0], [-1,-1],[-1,1], [1,-1 ]]
        q = deque([(0,0)])
        visited = [[False] * n for _ in range(m)]
        step = 0
        visited[0][0] = True
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x == m -1 and y == n-1:
                    return step
                for dir in dirs:
                    x_new = x + dir[0]
                    y_new = y + dir[1]
                    if 0 <= x_new < m and 0 <= y_mew < n and grid[x_new][y_new]
                    == 0 and not visited[x_new][y_new]:
                        q.append((x_new,y_new))
                        visited[x_new][y_new] = True
            step += 1
        return -1
