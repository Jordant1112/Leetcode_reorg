class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.d[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        for i in self.d[word1]:
            for j in self.d[word2]:
                res = min(res, abs(i - j))
        return res
