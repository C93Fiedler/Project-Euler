def Is_Prime(number):
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

def Prime_Factors(number):
    #assuming number is not even
    factors=[]
    counter=1
    while number!=1:
        counter+=2
        if Is_Prime(counter):
            if number%counter==0:
                factors.append(counter)
                number/=counter
                counter=1
##    for x in range(2,int(number/2)):
##        if Is_Prime(x):
##            if number%x==0:
##                factors.append(x)
    return factors

print Prime_Factors(13195)
print Prime_Factors(600851475143)[-1]
