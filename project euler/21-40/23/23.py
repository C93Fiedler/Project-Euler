def Factors(number):
    factors=[1]
    counter=1
    limit=number/2
    while counter<limit:
        counter+=1
        if number%counter==0:
            factors.append(counter)     
    return factors

counter=0
factors=[]
while counter<28124:
    counter+=1
    factors.append(Factors(counter))
print "cunt"
abundants=[]
for x in range(0,len(factors)):
    factors[x]=sum(factors[x])
    if factors[x]>x+1:
        abundants.append(x+1)
print abundants[0:10]
twoabundants=[]
print "twat"
print len(abundants)
counter=0
for x in abundants:
    counter+=1
    for y in abundants[counter-1:]:
        twoabundants.append(x+y)
total=0
print max(twoabundants)
print twoabundants[0:10]
for x in range(1, 20165):
    if x not in twoabundants:
        print x
        total+=x
print total
