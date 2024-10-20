class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.d = defaultdict(list)
        self.maxLevel = 0
        res = 0
        self.dfs(item, 1)
        if not self.d:
            return 0
        for level in self.d.keys():
            res += (maxLevel - level + 1) * sum(d[level])
        return res


    def dfs(self, item, level):
        if not item:
            return
        self.maxLevel = max(self.maxLevel, level)
        if item.isInteger():
            self.d[level].append(item.getInteger())
        elif item.getList():
            self.dfs(item, level+1)

