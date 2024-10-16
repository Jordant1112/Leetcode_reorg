class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        m = len(s)
        n = len(t)
        if s == t or abs(m-n) > 1:
            return False
        changed = False
        while p1 < m and p2 < n:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                if changed:
                    return False
                changed = True
                if m == n:
                    p1 += 1
                    p2 += 1
                elif m > n:
                    p1 += 1
                else:
                    p2 += 1
        return True
