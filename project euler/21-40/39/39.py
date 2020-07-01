#gets to 840 eventually
bigtotal=0
answer=0
for p in range(10,1001):
    total=0
    for a in range(1,int(p/3)):
        for b in range(a,int(p)):
            for c in range(b,int(p)):
                if a**2+b**2==c**2 and a+b+c==p:
                    total+=1
    if total>bigtotal:
        bigtotal=0
        bigtotal+=total
        answer=p
        print p
print answer
        
