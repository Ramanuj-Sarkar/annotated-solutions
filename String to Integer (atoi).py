# Take in a string which may contain an integer
# and, from the start, analyze it as though trying to insert it
# into a 32-bit integer, meaning that you find the numerical part
# and you round it down to the MAX or up to the MIN if necessary
class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for 32-bit signed integer range
        MAX, MIN = 2**31 - 1, -2**31
        
        # Step 1: Skip leading whitespace
        new_s = s.strip()
        
        # Check if it's completely whitespace
        if not new_s:
            return 0
        
        # Step 2: Check for sign
        sign = -1 if new_s[0] == '-' else 1
        
        # Skip sign if it's there
        if new_s[0] in {'+', '-'}:
            new_s = new_s[1:]

        
        # Step 3: Read digits and convert
        res = 0
        for char in new_s:
            if not char.isdigit():
                break
            digit = int(char)
            res = res * 10 + digit
            
            if sign * res <= MIN:
                return MIN
            
            if sign * res >= MAX:
                return MAX
        
        # Step 4: Apply sign and return
        return sign * res
        
