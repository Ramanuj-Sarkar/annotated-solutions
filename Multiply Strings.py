# You have two strings which are the shape of positive numbers.
# You have to multiply them without directly turning them into integers.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m + n) # final number
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # literally multiply digits
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)

                # add to what was previously there
                carry, rem = divmod(mul + pos[i + j + 1], 10)

                pos[i + j] += carry  # carry, you have to keep adding to it
                pos[i + j + 1] = rem  # non-carry, it's the right value

        # you turn the list into a string
        # then delete the trailing zeroes at the beginning
        final = ''.join([str(x) for x in pos]).lstrip('0')

        # 0 * 0 results in empty string
        # which is false in Python
        # and non-empty string is true
        return final if final else '0'
