class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        res = 0
        q = deque()
        q.append(entrance)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        visited[entrance[0]][entrance[1]] = True
        while q:
            size = len(q)
            res += 1
            for i in range(size):
                x_old, y_old = q.popleft()
                for dir in dirs:
                    x = x_old +  dir[0]
                    y = y_old + dir[1]
                    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or visited[x][y] or maze[x][y] == '+':
                        continue
                    if x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1:
                        return res
                    visited[x][y] = True
                    q.append((x,y))
        return -1

            
