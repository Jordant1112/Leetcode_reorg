class Solution:
    def compareVersion(self, version1: str, version2: str) -> str:
        s1 = version1.split('.')
        s2 = version2.split('.')
        length = max(len(s1), len(s2))
        for i in range(length):
            v1 = int(s1[i]) if i < len(s1) else 0
            v2 = int(s2[i]) if i < len(s2) else 0
            if v2 < v1:
                return 1
            if v1 < v2:
                return -1
        return 0
