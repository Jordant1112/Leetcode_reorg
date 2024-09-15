class Solution:
    def findaRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        n = len(s)
        for i in range(n-9):
            seq =  s[i:i+10]
            if seq in seen:
                res.add(seq)
            seen.add(seq)
        return list(res)
