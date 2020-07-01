#TAKES FOREVER

def Distinct_Prime_Factors(number):
    factors=[]
    counter=1
    limit=number/2
    if number%2==0:
        factors=[2]
    while counter<limit:
        counter+=2
        if Is_Prime(counter):
            if number%counter==0:
                factors.append(counter)     
    return factors

def Is_Prime(number):
    if number==1:
        return False
    if number==2:
        return True
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

x=210
flag=True
while flag:
    x+=1
    if len(Distinct_Prime_Factors(x))==4:
        if len(Distinct_Prime_Factors(x+1))==4:
            if len(Distinct_Prime_Factors(x+2))==4:
                if len(Distinct_Prime_Factors(x+3))==4:
                    flag=False              
print x
