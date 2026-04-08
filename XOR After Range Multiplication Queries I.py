'''
Given array nums and queries where queries are like [l, r, k, v]
for each query, you must:
1. set index to l
2. while index <= r
2.1 update nums[index] to be (nums[index] * v) % (1_000_000_007)
2.2 add k to index

Then you return the bitwise XOR of all the elements.

The problem is that this takes a long time.
This is why using Numpy is very important to save time in this context.
'''

import numpy as np
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # nums are an int64 array to stop overflow before mod
        arr = np.array(nums, dtype=np.int64)
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            # creates slice from l to r with step k
            # as well as taking mod in the correct way
            arr[l:r+1:k] = (arr[l:r+1:k] * v) % MOD
        
        # numpy also speeds up bitwise XOR
        # instead of naively using ^= on itself
        return int(np.bitwise_xor.reduce(arr))
