'''
You are given a stream of records about a particular stock.

Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Another record with the same timestamp may appear later in the stream
correcting the price of the previous wrong record.

You make an algorithm that:
* update() can update the stock price or correct it
* current() finds the latest price (the price at the latest timestamp)
* maximum() finds the maximum price the stock has had based on the records
* minimum() finds the minimum price the stock has had based on the records
'''
class StockPrice:
    def __init__(self):
        self.latest_time = 0
        # Store price of each stock at each timestamp.
        self.timestamp_price_map = {}
        
        # Store stock prices in sorted order to get min and max price.
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update latestTime to latest timestamp.
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        # Add latest price for timestamp.
        # Use negative prices for maxheap because heapq is a minheap
        # and it's easier to work around that.
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Return latest price of the stock.
        return self.timestamp_price_map[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while -price != self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
            
        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
            
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
