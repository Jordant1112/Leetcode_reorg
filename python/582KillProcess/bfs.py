class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) ->
    List[int]:
        graph = defaultdic(list)
        for i in range(len(pid)):
            child = pid[i]
            parent = ppid[i]
            graph[parent].append(child)

        q = deque()
        q.append(kill)
        res.append(kill)
        while q:
            cur = q.popleft()
            if cur in graph:
                for child in graph[cur]:
                    res.append(child)
                    q.append(child)
        return res
