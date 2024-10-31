class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        if rowIndex == 0:
            return res[0]
        for r in range(1, rowIndex+1):
            if r == 1:
                res.append([1,1])
            else:
                tmp = []
                tmp.append(1)
                for j in range(len(res[-1])-1):
                    tmp.append(res[-1][j] + res[-1][j+1])
                tmp.append(1)
                res.append(tmp)
        return res[rowIndex]
