# Given a string s and a wordDict of smaller strings
# return whether or not the string can be made using those words
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The answer is found using a cache.
        # This memoized object records the answer for the function
        # so the function doesn't need to be run multiple times to get the same result.
      
        @cache
        def dp(i):
            # We've reached the beginning of s
            if i < 0:
                return True

            for word in wordDict:
                # we check if the end of the word == word
                # and we check if dp(i - len(word)) is true
                # since dp(i - len(word)) is a smaller subproblem
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True
                
            # we failed to find a match
            return False

        return dp(len(s) - 1)
