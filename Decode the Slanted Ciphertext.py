# It starts with original text and a matrix with a fixed number of rows
# The original text is put in the matrix in a diagonal manner
# with each diagonal coming in the cells immediately after the previous.
# The leftmost column of the result contains the first character of originaltext
# at the top row and that's the only character it contains.
# The rightmost column is chosen so it won't be empty.
# The original text has no trailing spaces and all empty cells in the matrix
# are filled with spaces.
# The encoded text is created by reading the rows of the matrix into a string.
# We have to find the original text.
#
# Example:
# "cipher" in a matrix with 3 rows becomes:
# |ch  |
# | ie |
# |  pr|
# encoded becomes "ch   ie   pr"
# we are given encodedText = "ch   ie   pr", rows = 3, and have to remake "cipher"
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        encoded_length = len(encodedText)
        cols = encoded_length//rows  # this essentially indicates the amount of text in the first row
        s = ''  # result text
        
        for i in range(cols):  
            j = i
            while j<encoded_length:
                s+=encodedText[j]
                j += cols + 1  # you skip to the cell underneath, then go one right because it's diagonal
        
        return s.rstrip()
  
