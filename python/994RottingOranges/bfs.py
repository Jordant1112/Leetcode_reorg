class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = [[-1, 0], [1, 0], [0, -1], [0,1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for dir in dirs:
                    x_new, y_new = x + dir[0], y + dir[1]
                    if x_new < 0 or y_new < 0 or x_new >= len(grid) or y_new >= len(grid[0]) or grid[x_new][y_new] == 2:
                        continue
                    if grid[x_new][y_new] == 1:
                        grid[x_new][y_new] = 2
                        q.append((x_new, y_new))
            step += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return step -1 if step else 0
