import random
class Solution:
    def __init__(self):
        self.res = []
        self.valToIndex = {}
        self.r = random

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        self.valToIndex = len(self.res)
        self.res.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False
        idx = self.valToIndex[val]
        element = self.res[-1]
        self.valToIndex[element] = idx
        self.res[idx], self.res[-1] = self.res[-1], self.res[idx]
        self.res.pop()
        del self.valToIndex[val]
        return True

    def getrandom(self) -> int:
        random = self.r.randint(0, len(self.res) -1)
        return self.res[random]
