def Is_Prime(number):
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True
counter=1
for x in range(2,1000000):
    flag=True
    if Is_Prime(x):
        cunt=str(x)
        for char in range(1, len(cunt)):
            cunt=cunt[1:]+cunt[0]
            if not Is_Prime(int(cunt)):
                flag=False
    else: flag=False
    if flag:
        counter+=1
print counter
    
            
            
