class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] *n
        q = deque([0])
        visited[0] = True
        while q:
            size = len(q)
            for i in range(size):
                r = q.popleft()
                for nextroom in rooms[r]:
                    if not visited[nextroom]:
                        visited[nextroom] = True
                        q.append(nextroom)
        for v in visited:
            if not v:
                return False
        return True
