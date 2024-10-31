class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return [[1]]
        for r in range(2, numRows+1):
            if r == 2:
                res.append([1,1])
            else:
                tmp = []
                tmp.append(1)
                for j in range(len(res[-1])-1):
                    tmp.append(res[-1][j] + res[-1][j+1])
                tmp.append(1)
                res.append(tmp)
        return res
