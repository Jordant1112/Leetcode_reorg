class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        q = deque()
        g = defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        for i in range(n):
            if len(g[i]) == 1:
                q.append(i)

        node_count = n
        while node_count > 2:
            size = len(q)
            node_count -= size
            for i in range(size):
                r = q.popleft()
                for neighbor in g[r]:
                    g[neighbor].remove(r)
                    if len(g[neighbor]) == 1:
                        q.append(neighbor)
        return list(q)
