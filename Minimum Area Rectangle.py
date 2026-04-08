# find the smallest rectangle made by the points in question
# return 0 if none is found
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # puts the points in an easily-queryable state
        columns = collections.defaultdict(list)

        for x, y in points:
            columns[x].append(y)
        
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]

            # sort it so you get the smaller ones before the other ones
            column.sort()
            for j, y2 in enumerate(column):
                # find ones with a lower y value
                for y1 in column[:j]:
                    # you now have 3 points

                    if (y1, y2) in lastx:
                        # you have 4 points
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    
                    # the fourth point is the new third point
                    # since going past this won't be the minimum
                    lastx[y1, y2] = x
        
        # return 0 if nothing is found
        return ans if ans < float('inf') else 0
        
