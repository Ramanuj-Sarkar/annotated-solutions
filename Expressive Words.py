# You have the final string s.
# For each word in words, you have to see if it can become like s.
# Every group of the same char in each word can be extended to a group of 3 or more.
# It can't be extended to a group of 2.
# This is the only change you can make to each word.
# You return the number of words which can become like s.
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(self.compare(word, s) for word in words)
    
    def compare(self, s1: str, s2: str) -> int:
        i, j = 0, 0  # point in first string / second string
        
        while i < len(s1):
            # either the end of s2 has been reached
            # or s1 and s2 have different characters here
            if j >= len(s2) or s1[i] != s2[j]:
                return 0
            
            l1, l2 = 0, 0  # number of repetitions
            c = s1[i]  # the char in question

            while i < len(s1) and s1[i] == c:
                l1 += 1
                i += 1
            
            while j < len(s2) and s2[j] == c:
                l2 += 1
                j += 1

            # you can't take away characters
            # or turn a group of 1 in l2 into a group of 2
            if l1 > l2 or (l2 < 3 and l2 != l1):
                return 0

        # you have to reach the end of both
        if j != len(s2):
            return 0
        
        return 1 
