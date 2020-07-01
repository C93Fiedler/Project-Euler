#brute force to max
cunt=[]
a=0
while a<5000:
    a+=1
    b=a
    while b<5000:
        b+=1
        if len(str(a))+len(str(b))+len(str(a*b))==9:
            total=0
            if "1" in (str(a) +str(b) +str(a*b)):
                if "2" in (str(a) +str(b) +str(a*b)):
                    if "3" in (str(a) +str(b) +str(a*b)):
                        if "4" in (str(a) +str(b) +str(a*b)):
                            if "5" in (str(a) +str(b) +str(a*b)):
                                if "6" in (str(a) +str(b) +str(a*b)):
                                    if "7" in (str(a) +str(b) +str(a*b)):
                                        if "8" in (str(a) +str(b) +str(a*b)):
                                            if "9" in (str(a) +str(b) +str(a*b)):
                                                if a*b not in cunt:
                                                    cunt.append(a*b)
print sum(cunt)

