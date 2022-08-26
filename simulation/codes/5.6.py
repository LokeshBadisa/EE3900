from sympy import Sum,var


def usf(n):
        return 1
   

def h(n):
    return ((-0.5)**(n))*usf(n) + ((-0.5)**(n-2))*usf(n-2)

var("n")
expr1 = Sum(h(n),(n,0,float('inf')))
print(expr1.doit())



 