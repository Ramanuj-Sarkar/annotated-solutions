from typing import List

# You have an array of integers and an array of queries.
# For each query, which is structured like [1, r, k, v]:
# 1. Set idx to l:
# 2. While idx <= r:
# 2.1 Update nums[idx] to (nums[idx] * v) % (1,000,000,007).
# 2.2 Add k to idx.
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # working array, will be modified in place
        ans = nums[:]

        # when k >= sqrt(n), the query touches < sqrt(n) elements
        # when k < sqrt(n), this is not true
        # we need to put these cases in two groups and treat them differently
        B = int(n**0.5) + 1

        # separate queries according to step size
        large = []                     # k > B
        small_by_k = [[] for _ in range(B + 1)]   # k <= B, index by k

        for l, r, k, v in queries:
            if k > B:
                # we can brute_force it
                large.append((l, r, k, v))
            else:
                # we will need to be tactical
                small_by_k[k].append((l, r, v))

        # ---------- process large steps (brute force) ----------
        for l, r, k, v in large:
            idx = l
            while idx <= r:
                ans[idx] = (ans[idx] * v) % MOD
                idx += k

        # ---------- process small steps (offline per k) ----------
        for k in range(1, B + 1):
            ev_list = small_by_k[k]
            if not ev_list:
                continue

            # group events by remainder modulo k
            rem_events = [[] for _ in range(k)]
            for l, r, v in ev_list:
                rem = l % k
                L = (l - rem) // k
                R = (r - rem) // k
                rem_events[rem].append((L, R, v))

            # handle each remainder that actually appears
            for rem in range(k):
                events = rem_events[rem]
                if not events:
                    continue

                # number of indices with this remainder
                size = (n - 1 - rem) // k + 1   # >= 1

                # build actions: (position, v, is_end)
                actions = []
                for L, R, v in events:
                    actions.append((L, v, False))          # start
                    if R + 1 < size:
                        actions.append((R + 1, v, True))   # end (apply inverse)

                actions.sort(key=lambda x: x[0])

                cur = 1
                act_idx = 0
                num_act = len(actions)

                # sweep over all positions of this remainder
                for p in range(size):
                    while act_idx < num_act and actions[act_idx][0] == p:
                        _, v, is_end = actions[act_idx]
                        if is_end:
                            inv = pow(v, MOD - 2, MOD)
                            cur = (cur * inv) % MOD
                        else:
                            cur = (cur * v) % MOD
                        act_idx += 1

                    idx = rem + p * k
                    ans[idx] = (ans[idx] * cur) % MOD

        # ---------- compute final xor ----------
        xor_result = 0
        for val in ans:
            xor_result ^= val
        return xor_result
