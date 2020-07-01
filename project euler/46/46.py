def Is_Prime(number):
    if number==1:
        return False
    if number==2:
        return True
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

def hi(number):
    for x in range(2,number-1):
        counter=0
        if Is_Prime(x):
            while x+2*counter**2<number:
                counter+=1
                if x+2*counter**2==number:
                    return True
    return False
                
    
flag=True
x=31
while flag:
    x+=2
    if not Is_Prime(x):
        flag=hi(x)
print x
