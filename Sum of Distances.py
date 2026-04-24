'''
You are given a 0-indexed integer array nums.

There exists an array arr of length nums.length,
where arr[i] is the sum of |i - j| over all j
such that nums[j] == nums[i] and j != i.

If there is no such j, set arr[i] to be 0.

Return the array arr.
'''
class Solution:
    def distance(self, nums):
        n = len(nums)
        answer = [0] * n

        # places which have the same value
        same_val = defaultdict(list)
        for i in range(n):
            same_val[nums[i]].append(i)


        for arr in same_val.values():
            siz = len(arr)

            # prefix sum array
            pref = [0] * siz
            pref[0] = arr[0]
            
            # find the next value at each point
            for i in range(1, siz):
                pref[i] = pref[i - 1] + arr[i]

            # find distance to elements on either side
            for i in range(siz):
                left = 0
                right = 0

                if i > 0:
                    # we want: (arr[i] - arr[0]) + (arr[i] - arr[1]) + ... + (arr[i] - arr[i-1])
                    # thing below = i * arr[i] − (sum of all left elements)
                    left = i * arr[i] - pref[i - 1]

                if i < siz - 1:
                    # we want: (arr[i+1] - arr[i]) + (arr[i+2] - arr[i]) + ...
                    # thing below = (sum of right elements) − (element count * arr[i])
                    right = (pref[siz - 1] - pref[i]) - (siz - i - 1) * arr[i]

                # efficiently gives total distance to all same elements
                answer[arr[i]] = left + right

        return answer
