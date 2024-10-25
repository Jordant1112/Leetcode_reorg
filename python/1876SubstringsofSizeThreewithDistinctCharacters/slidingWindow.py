class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 3 + 1):
            d = {}
            for j in range(3):
                if s[i+j] not in d:
                    d[s[i+j]] = 1
                else:
                    d[s[i+j]] += 1
            if len(d) == 3:
                res += 1
        return res
