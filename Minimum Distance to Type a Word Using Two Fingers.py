'''
The keyboard is like:
a b c d e f
g h i j k l
m n o p q r
s t u v w x
y z

Return the minimum total distance to type the sttring
using only two fingers
and the initial positions of your fingers are free
'''
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        # BIG is big enough to allow for the finding of a minimum
        BIG = 2**30

        # one hand is at word[i]
        # the other hand is at rest
        # think of dp[i][j] as dp[position of i][resting hand not on i]
        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]

        # this is just how you get the distance from numbers
        # using coordinates like:
        # 0 = A -> (0,0)
        # 1 = B -> 
        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)


        for i in range(1, n):  # all the letters in words
            # current is position of current letter on hand #1
            # prev is position of previous letter
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)


            # this loop is for the hand that was at rest
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                if prev == j:  # we know hand #2 was here
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        # what if hand #2 had moved to k in that time?
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)

        ans = min(dp[n - 1])
        return ans
      
