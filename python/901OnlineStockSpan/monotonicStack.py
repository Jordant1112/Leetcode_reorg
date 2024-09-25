class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, pre_span = stack.pop()
            cur_span += pre_span
        self.stack.append((price, cur_span))
        return cur_span
