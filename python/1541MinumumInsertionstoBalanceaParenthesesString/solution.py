class Solution:
    def minInsertions(self, s:str) -> str:
        res = 0
        need = 0
        for i in s:
            if i == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            if i == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return need + res
