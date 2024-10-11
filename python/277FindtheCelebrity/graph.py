class Solution:
    def findCelebrity(self, n: int) -> int:
        if n == 1:
            return 0
        q = deque([for i in range(n)])
        while q >= 2:
            cand = q.popleft()
            other = q.popleft()
            if not knows(other, cand) or knows(cand, other):
                q.appendleft(other)
            else:
                q.appendleft(hand)
        cand = q.popleft()
        for other in range(n):
            if other == cand:
                continue
            if not knows(other, cand) or knows(cand, other):
                return -1
        return can
