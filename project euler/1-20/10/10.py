def Is_Prime(number):
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

total=2
counter=3
while counter<2000000:
    if Is_Prime(counter):
        total+=counter
    counter+=2
print total
