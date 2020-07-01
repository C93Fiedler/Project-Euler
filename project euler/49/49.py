def Is_Prime(number):
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True
def Are_Permutations(numbers):
    charsets=[]
    for x in numbers:
        charsets.append([])
    counter=-1

    for number in numbers:
        counter+=1
        for char in str(number):
            charsets[counter].append(char)
    for sets1 in charsets:
        for char1 in sets1:
            for sets2 in charsets:
                if char1 not in sets2:
                    return False
    return True

for x in range(1001,10000):
    if Is_Prime(x):
        for y in range(2,3001,2):
            if Is_Prime(x+y):
                if Is_Prime(x+2*y):
                    if Are_Permutations([x,x+y,x+2*y]):
                        print x
                        print y
                        print "_______________________________"
                        print "_______________________________"
                        print "_______________________________"
                        print "_______________________________"
                        print "_______________________________"
                        print "_______________________________"
                        print "_______________________________"
