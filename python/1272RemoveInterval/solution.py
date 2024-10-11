class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            if i[0] >= toBeRemoved[1] or i[1] <= toBeRemoved[0]:
                res.append([i[0], i[1]])
            else:
                if i[0] < toBeRemoved[0]:
                    res.append([i[0], toBeRemoved[0]])
                if i[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], i[1]])
        return res


