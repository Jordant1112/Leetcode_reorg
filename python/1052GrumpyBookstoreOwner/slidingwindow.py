class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes:int) -> int:
        cur_benefit = customers[:minutes]
        res = cur_benefit
        start_optimal = 0
        for i in range(1, len(customers)- minutes + 1):
            end = i + minutes -1
            if grumpy[i] == 1:
                cur_benefit -= customers[i]
            if grumpy[end] == 1:
                cur_benefit += customers[i]
            if cur_benefit > res:
                res = cur_benefit
                start_optimal = i
        base = 0    
        for i in range(len(customners)):
            if grumpy[i] == 0 or start_optimal <= i < start_optimal + minutes:
                base += customers[i]
        return base
