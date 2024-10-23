class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        res = 0
        d = {}
        for i in range(k):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        if len(d) == k:
            res += 1
        for i in range(k, len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            d[s[i-k]] -= 1
            if d[s[i-k]] == 0:
                del d[s[i-k]]
            if len(d) == k:
                res += 1
        return res
