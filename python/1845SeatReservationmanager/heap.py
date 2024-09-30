class SeatManager:
    def __init__(self, n: int):
        self.pq = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        res = heapq.heappop(self.pq)
        return res

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)
