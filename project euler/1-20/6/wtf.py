def Sum(n,lim):
    total=0
    for x in range(1,lim+1):
        total+=x**n
    return total

n1=Sum(1,100)
n2=Sum(2,100)
print n1
print n2
print str(n1**2-n2)
