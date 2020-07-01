def Is_Pentagonal(x):
    n=(1+(1+24*x)**0.5)/6
    if n==int(n):
        return True
    return False

def Is_Hexagonal(x):
    n=(1+(1+8*x)**0.5)/4
    if n==int(n):
        return True
    return False

x=285
t=x*(x+1)/2
flag=True
while flag:
    x+=1
    t=x*(x+1)/2
    if Is_Hexagonal(t):
        if Is_Pentagonal(t):
            print t
            flag=False
