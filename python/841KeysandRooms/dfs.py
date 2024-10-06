class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)
        for v in visited:
            if not v:
                return False
        return True
    


    def dfs(self, rooms, i, visited):
        if not visited[i]:
            visited[i] = True
        for nei in rooms[i]:
            if not visited[nei]:
                self.dfs(rooms, nei, visited)

