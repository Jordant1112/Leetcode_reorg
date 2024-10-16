class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while j < len(chars):
            count = 0
            curr = chars[j]
            while j < len(chars) and chars[j] == curr:
                count += 1
                j += 1
            chars[i] = curr
            i += 1
            if count > 1:
                for d in str(count):
                    chars[i] = d
                    i += 1
            return i
                
