def Pn(n):
    return 0.5*n*(3*n-1)
def Is_Pentagonal(x):
    n=(1+(1+24*x)**0.5)/6
    if n==int(n):
        return True
    return False

counter=3
p=[Pn(1),Pn(2),Pn(3)]
flag=True
while flag:
    counter+=1
    p.append(Pn(counter))
    counter2=-1
    for x in p:
        counter2+=1
        for y in p[:counter2]:
            if Is_Pentagonal(x+y):
                if Is_Pentagonal(x-y):
                    print x
                    print y
                    flag=False
