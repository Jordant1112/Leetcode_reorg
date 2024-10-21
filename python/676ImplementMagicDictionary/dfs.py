class MagicDictionary:
    def __init__(self):
        self.d = {}

    def buidlDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                replaced = word[:i] + '*' + word[i+1:]
                if replaced in self.d:
                    self.d[replaced].append(word)
                else:
                    self.d[replaced] = [word]

    def search(self, searchWord: str) -> bool:
        for i in range(len(serachWord)):
            replaced = searchWord[:i] + '*' + searchWord[i+1:]
            if replaced in self.d:
                words = self.d[replaced]
                for word in words:
                    if word != searchWord and len(word) == len(searchWord):
                        match = True
                        for j in range(len(searchWord)):
                            if searchWord[j] != word[j] and replaced[j] != '*':
                                match = False
                                break
                        if match:
                            return True
        return False

