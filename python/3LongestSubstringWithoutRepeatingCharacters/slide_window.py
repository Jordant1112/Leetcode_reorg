class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
                while d[s[i]] > 1:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        del d[s[j]]
                    j += 1
            res = max(res, len(d))
        return res
