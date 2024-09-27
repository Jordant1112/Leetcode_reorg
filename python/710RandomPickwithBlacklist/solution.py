import random
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = {}
        self.r = random
        self.size = n - len(blacklist)
        blackset = set(blacklist)
        last = n - 1
        for b in blacklist:
            if b >= self.size:
                continue
            while last in blackset:
                last -= 1
            self.mapping[b] = last
            last -= 1

    def pick(self):
        r = self.r.randint(0, self.size-1)
        if r in self.mapping:
            return self.mapping[r]
        return r
