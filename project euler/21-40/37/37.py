def Is_Prime(number):
    if number==1:
        return False
    if number==2:
        return True
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

counter=10
total=0
counter2=0
while counter2<11:
    counter+=1
    if Is_Prime(counter):
        flag=True
        for x in range(1,len(str(counter))):
            if not Is_Prime(int(str(counter)[x:])):
                flag=False
            if not Is_Prime(int(str(counter)[:x])):
                flag=False
        if flag:
            counter2+=1
            total+=counter
            print counter
print total
