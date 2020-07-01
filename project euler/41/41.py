def Is_Prime(number):
    for x in range(2, int((number)**0.5)):
        if number%x==0:
            return False
    return True
flag=False
x=10000000
while not flag:
    x-=1
    if Is_Prime(x):
        flag=True
        for digit in range(1, len(str(x))+1):
            
            if str(digit) not in str(x):
                flag=False
print x
