class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) ->
    int:
        if True not in hasApple:
            return 0
        self.graph = defaultdict(list)
        for i, j in edges:
            self.graph[i].append(j)
            self.graph[j].append(i)
        res = self.dfs(0, None, hasApple)
        return res - 2 if res else 0

    def dfs(self, node, parent, hasApple):
        steps = 0
        for child in self.graph[node]:
            if child != parent:
                steps += self.dfs(child, node, hasApple)
        return steps + 2 if steps or hasApple[node] else 0
