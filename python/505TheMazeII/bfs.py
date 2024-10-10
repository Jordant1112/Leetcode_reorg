class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        q = deque()
        q.append(start)
        memo = [[-1] * n for _ in range(m)]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        memo[start[0]][start[1]] = 0
        while q:
            cur = q.popleft()
            for dir in dirs:
                x = cur[0]
                y = cur[1]
                step = memo[x][y]
                x_new = x + dir[0]
                y_new = y + dir[1]
                while 0 <= x_new < m and 0 <= y_new < n and maze[x_new][y_new] == 0:
                    x = x_new
                    y = y_new
                    step += 1
                    x_new += dir[0]
                    y_new += dir[1]
                if memo[x][y] == -1 or memo[x][y] > step:
                    memo[x][y] = step
                    q.append((x,y))
        return memo[destination[0]][destination[1]]
