from math import factorial
def subsets_parity(n,k):
    n_fact = 1
    b_n, b_k = bin(n)[2:], bin(k)[2:]
    if len(b_k) < len(b_n):
        b_k = '0' * (len(b_n) - len(b_k)) + b_k
    
    print(n, b_n, k, b_k)
    
    for digits in zip(b_n, b_k):
        print(digits)
        if digits[0] == '0' and digits[1] == '1':
            return 'EVEN'
    return 'ODD'
