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
  
