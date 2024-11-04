from sortedcontainers import SortedList
class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        depths = {float('inf'):0, float('-inf'):0}
        sl = SortedList([float('inf'),float('-inf')])
        for x in order:
            i = sl.bisect_left(x)
            depths[x] = 1 + max(depths[sl[i-1]], depths[sl[i]])
            print(i)
            print(depths)
            sl.add(x)
            print(sl)
        return max(depths.values())
