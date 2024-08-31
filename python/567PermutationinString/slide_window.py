class Solution:
    def checkInclusion(self, s1, s2) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        l, valid = 0, 0
        for i in s1:
            d1[i] += 1
        for i in range(len(s2)):
            if s2[i] in d1:
                d2[s2[i]] += 1
                if d2[s2[i]] == d1[s1[i]]:
                    valid += 1
            while (i - l + 1 >= len(s1)):
                if valid == len(d1):
                    return True
                if s2[l] in d1:
                    if d2[s2[i]] == d1[s2[i]]:
                        valid -= 1
                    d2[s2[i]] -= 1
                l += 1
        return False
