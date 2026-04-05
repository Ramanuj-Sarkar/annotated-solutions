# You get a string like "2[a]3[bc]"
# You have to decode the string in the brackets as many times as the number before
# "2[a]3[bc]" -> aabcbcbc
# "2[a3[b]]" -> abbbabbb
# You return that string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == ']':
                # add the string being copied within [ and ]
                decoded = ''
                while stack[-1] != '[':
                    decoded += stack.pop()
                stack.pop()
                
                # get the value of k
                base, k = 1, 0
                while stack and stack[-1].isdigit():
                    k += base * (ord(stack.pop()) - 48)
                    base *= 10
                
                # repeatedly append that thing
                for _ in range(k):
                    for j in range(len(decoded) - 1, -1, -1):
                        stack.append(decoded[j])
            else: # normal procedure
                stack.append(char)
        
        return ''.join(stack)
  
