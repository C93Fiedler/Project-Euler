def Is_Prime(number):
    try:
        for x in range(2, int((number)**0.5)+2):
            if number%x==0:
                return False
        return True
    except Exception:
        pass

longest=0
for a in range (-999,1000):
    for b in range (-999,1000):
        n=0
        while Is_Prime(n**2+a*n+b):
            n+=1
        if n>longest:
            longest=0
            longest+=n
            result=a*b
print result
