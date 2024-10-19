class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
            worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        profit = 0
        best = 0
        j = 0
        for ability in worker:
            while j < len(worker) and ability >= jobs[j][0]:
                profit = max(profit, jobs[j][1])
                j += 1
            best += profit
        return best
