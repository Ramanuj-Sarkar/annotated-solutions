class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Use a min-heap to store the points based on their distance
        h = []
        for point in points: # n 
            x = point[0]
            y = point[1]
            d = x * x + y * y
            heapq.heappush(h, (d, point)) # heap size: n

        # Extract the k closest points
        ans = []
        for i in range(k): # k
            first_pt_d, first_pt = heapq.heappop(h) # heap size: n
            ans.append(first_pt)
        return ans
