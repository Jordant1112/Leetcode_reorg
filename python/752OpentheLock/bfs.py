class Solution:
    def openLock(self, deadends: List[str], target:str) -> int:
        visited = set()
        q = deque(['0000'])
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                key = q.popleft()
                if key == target:
                    return step
                if key not in visited and key not in deadends:
                    for i in range(4):
                        m1 = self.minusone(key, i)
                        p1 = self.plusone(key, i)
                        q.append(m1)
                        q.append(p1)
            step += 1
        return -1

    def minusone(self, key, i):
        if key[i] == '0':
            s = key[:i] + '9' + key[i+1:]
        else:
            s = key[:i] + str(int(key[i]-1)) + key[i+1:]
        return s

    def plusone(self, key, i):
        if key[i] == '9':
            s = key[:i] + '0' + key[i+1:]
        else:
            s = key[:i] + str(int(key[i]+1)) + key[i+1:]
        return s
