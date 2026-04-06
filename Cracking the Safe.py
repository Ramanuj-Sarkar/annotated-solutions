# the safe has digits from 0 to k-1
# it checks if the last n entries form the correct password
# n is between 1 and 4
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # satisfies the case of the password being all 0s
        ans = "0" * (n - 1)
        visits = set()
        
        # there can be k ** n passwords
        for x in range(k ** n):
            
            # find the last n - 1 digits
            # if n == 1, it's an empty string
            current = '' if n == 1 else ans[-(n-1):]
            
            for y in range(k - 1, -1, -1):
                # current + str(y) is the last n digits
                # if the last n digits haven't been seen, add this last digit
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans
