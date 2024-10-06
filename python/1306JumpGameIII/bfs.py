class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        q = deque([start])
        n = len(arr)
        visited = [False]*n
        visited[start] = True
        while q:
            r = q.popleft()
            plus = r + arr[r]
            minus = r - arr[r]
            if arr[r] == 0:
                return True
            if plus < n and not visited[plus]:
                visited[plus] = True
                q.append(plus)
            if minus >= 0 and not visited[minus]:
                visited[minus] = True
                q.append(minus)
        retrurn False
