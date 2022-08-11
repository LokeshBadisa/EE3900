from sympy import limit,Symbol

def usf(n,k):]\
    if n < k :
        return 0
    else:
        return 1

def h(n,k):
    return ((-0.5)**(n+k))*usf(n,k) + ((-0.5)**(n-2+k))*usf(n,2+k)

n = Symbol('n') 
L = h(n,1)/h(n,0)
final=limit(L, n, 0)

print(final)

if(abs(final)<1):
    print("Convergent")
else:
    print("Divergent")    