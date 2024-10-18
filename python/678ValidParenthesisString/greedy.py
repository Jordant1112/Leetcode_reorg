class Solution:
    def checkValidString(self, s: str) -> bool:
        countmin = countmax = 0
        for i in s:
            if i == '(':
                countmin += 1
                countmax += 1
            elif i == ')':
                countmin -= 1
                countmax -= 1
            else:
                countmin -= 1
                countmax += 1
            if countmax < 0:
                return False
            if countmin < 0:
                countmin = 0
        return countmin == 0
