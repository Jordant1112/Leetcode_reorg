class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addnum(self, num: int) -> None:
        if len(self.small) >= len(self.large):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.lagre[0]) / 2.0
