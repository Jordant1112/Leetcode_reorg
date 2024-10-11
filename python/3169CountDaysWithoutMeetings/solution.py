class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        merge = [meetings[0]]
        for m in meetings[1:]:
            if m[0] <= merge[-1][1]:
                merge[-1][1] = max(m[1], merge[-1][1])
            else:
                merge.append(m)
        res = 0
        for i, j in merge:
            res += j-i + 1
        return days - res
        
