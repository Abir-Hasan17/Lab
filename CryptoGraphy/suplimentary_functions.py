def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp>0:
        if exp%2 ==1:
            res = (res*base) % mod
        base = (base*base) % mod
        exp = exp//2
    return res

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a>1:
        q = a//m
        a, m = m, a%m
        x0, x1 = x1 - q*x0, x0
    
    return x1%m0


print(modular_inverse(5,6))
print(pow(5,-1,6))