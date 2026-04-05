# Given n pairs of parentheses
# return a list of all well-formed combinations of parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_strings = []

        def add_paren(open, close, final):
            if len(final) == n * 2:
                all_strings.append(final)  # the string is ensured to be well-formed
            else:
                if open < n:  # any number of these opens can be added
                    add_paren(open + 1, close, final + '(')
                
                if close < open:  # closes can be added if they come after opens
                    add_paren(open, close + 1, final + ')')
        
        add_paren(0, 0, '')

        return all_strings
