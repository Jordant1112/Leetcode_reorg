class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for l in image:
            l.reverse()
        res = []
        for l in image:
            tmp = []
            for ele in l:
                if ele == 0:
                    tmp.append(1)    
                else:
                    tmp.append(0)
            res.append(tmp)
        return res
