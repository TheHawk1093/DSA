class StockSpanner:

    def __init__(self):
        self.span = []
        

    def next(self, price: int) -> int:
        if not self.span:
            self.span.append((price,1))
            return 1
        
        updated_span = 1
        while self.span and self.span[-1][0] <= price:  
            old_price,span = self.span.pop()
            updated_span += span
        self.span.append((price,updated_span))
        return updated_span
    


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)