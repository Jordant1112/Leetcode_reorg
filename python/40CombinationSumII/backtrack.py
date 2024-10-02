class Solution:
    def combinationSum2(self, candidates: List[int], target: int) ->
    List[List[int]]:
        res = []
        output = []
        candidates.sort()
        self.backtrack(candidates, res, output, target, 0)
        return res

    def backtrack(self, candidates, res, output, target, start):
        if sum(output) == target:
            res.append(output)
            return
        if sum(output) > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.backtrack(candidates, res, output+ [candidates[i]], target,
                    i+1)

