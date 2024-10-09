class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x = jug1Capacity
        y = jug2Capacity
        z = targetCapacity
        q = deque([0])
        visited = set()
        move = [x,-x,y,-y]
        while q:
            cap = q.popleft()
            if cap == z:
                return True
            for m in move:
                new_cap = cap + m
                if new_cap < 0 or new_cap > x + y or new_cap in visited:
                    continue
                visited.add(new_cap)
                q.append(new_cap)
        return False
