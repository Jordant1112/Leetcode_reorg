class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        tmp = []
        i = total = res = 0
        for i in range(len(s)):
            tmp.append(abs(ord(s[i]) - ord(t[i])))
        for j in range(len(tmp)):
            total += tmp[j]
            while total > maxCost and i <= j:
                total -= nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res
