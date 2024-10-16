class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = []
        tmp = ''
        for i in range(len(s)):
            if s[i] != ' ':
                tmp += s[i]
            elif s[i] == ' ':
                res.append(tmp)
                tmp = ''
            if i == len(s)-1:
                res.append(tmp)
        inverse = []
        for i in range(len(res)-1, -1, -1):
            for letter in res[i]:
                inverse.append(letter)
            if i != 0:
                inverse.append(" ")
        s[:] = inverse
        return inverse

