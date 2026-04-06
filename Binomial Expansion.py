import re
from math import prod, factorial

# takes in a string expression like (ax+b)^n
# returns the expanded version of this
def expand(expr):
    # splits on variable
    exprlist = re.split('[A-z]', expr)

    # finds a, b, and n respectively
    exprlist = [exprlist[0][1:], exprlist[1][:-1], exprlist[2]]

    # makes sure a is a number
    if exprlist[0] in ('', '-'):
        exprlist[0] += '1'
    
    a, b, n = [int(x) for x in exprlist]

    # finds variable
    x = re.findall('[A-z]', expr)[0]

    # if n == 0
    if not n:
        return '1'
    
    n1 = n+1
    
    vals = [(n-i, i) for i in range(n1)]
    
    # prod() is like sum() but for multiplication
    # this computes the correct row of Pascal's triangle
    pattern = [prod(_ for _ in range(max(i)+1, n1)) // factorial(min(i)) for i in vals]

    # this multiplies the values in Pascal's triangle by the correlated values
    # and creates a list of coefficients
    coefs = [(a ** vals[i][0] * b ** vals[i][1] * pattern[i]) for i in range(n1)]

    # the enumerate allows you to quickly get the index and the number
    # the first part of the string checks if this is the beginning or not / adds or subtracts
    # the second part adds the coefficient
    # the third part adds the variable
    # the fourth part adds ^n if it should be there (so not for the last two)
    terms = ''.join([f'{"-" if coefs[i[0]] < 0 else "" if i[0] == 0 else "+"}'
                     f'{abs(coefs[i[0]]) if (abs(coefs[i[0]]) != 1 or i[1] == 0) else ""}'
                     f'{x if i[1] > 0 else ""}'
                     f'{"^" + str(i[1]) if i[1] > 1 else ""}'
                     for i in enumerate(range(n,-1,-1))])
    
    return terms
