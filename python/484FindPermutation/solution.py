class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        res = [i for i in range(1,n+1)]
        i = 0
        while i < len(s):
            if s[i] == 'D':
                j = i
                while i < len(s) and s[i] == 'D':
                    i += 1
                res[j:i+1] = reversed(res[j:i+1])
            else:
                i += 1
        return res