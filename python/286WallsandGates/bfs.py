class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        step = 0
        while q:
            x, y = q.popleft()
            for dir in dirs:
                x_new = x + dir[0]
                y_new = y + dir[1]
                if 0 <= x_new < m and 0 <= y_new < n and rooms[x_new][y_new] == 2147483647:
                    rooms[x_new][y_new] = rooms[x][y] + 1
                    q.append((x_new, y_new))
        return rooms

