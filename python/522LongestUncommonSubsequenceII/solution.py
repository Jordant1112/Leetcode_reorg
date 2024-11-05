class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key = lambda x: -len(x))
        for i, word in strs:
            if all(not self.helper(word, strs[j]) for j in range(len(strs)) if j
                != i):
                return len(word)
        return -1

    def helper(self, w1, w2):
        if len(w1) > len(w2):
            return False
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)
