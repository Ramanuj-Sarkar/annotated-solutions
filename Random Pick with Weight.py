'''
You get a 0-indexed array of positive integers.
The integers in the array describe the weight of each index.
Implement pickindex, which randomly picks an index in the range.
The probability of picking the index is w[i] / sum(w).

[1,3] - the probability of picking 0 is 1/4 and the probability of 1 is 3/4
'''
class Solution:

    def __init__(self, w: List[int]):
        self.sums = [w[0]]

        # Gets all the sums.
        # Think of prefix sums as Cumulative Distribution Function(CDF).
        for weight in w[1:]:
            self.sums.append(self.sums[-1] + weight)
        
        self.total_sum = self.sums[-1]
        

    def pickIndex(self) -> int:
        random_value = random.randint(1, self.total_sum)  # import random

        # bisects the first value at the point
        # the second value is less than or equal to the index
        return bisect.bisect_left(self.sums, random_value)  # import bisect
