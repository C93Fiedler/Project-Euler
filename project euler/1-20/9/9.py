def findabc():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if a**2+b**2==c**2:
                    if a+b+c==1000:
                        return [a,b,c]

    return "cunt"
print findabc()
##[200, 375, 425]
