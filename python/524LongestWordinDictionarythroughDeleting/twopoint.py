class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        r = ''
        for word in dictionary:
            i , j = 0, 0
            while i < len(word) and j < n:
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                if r == '' or len(word) > len(r):
                    r = word
                elif len(r) > 1 and len(r) == len(word) and word < r:
                    r = word
        return r 
            
                        
