class StockSpanner:

    def __init__(self):
        self.stocks_price = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.stocks_price and self.stocks_price[-1][0]<=price :
            prev_stock_price,prev_stock_span = self.stocks_price.pop()
            span += prev_stock_span
        self.stocks_price.append((price,span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)