def Factors(number):
    factors=[1]
    counter=1
    limit=number/2+2
    while counter<limit:
        counter+=1
        if number%counter==0:
            factors.append(counter)     
    return factors

counter=0
factors=[]
while counter<10000:
    counter+=1
    factors.append(Factors(counter))
for x in range(0,len(factors)):
    factors[x]=sum(factors[x])
counter=0
numbers=[]
for x in range(0,len(factors)-1):
    counter+=1
    counter2=x+1
    for y in range(x+1, len(factors)):
        counter2+=1
        if x+1==factors[y] and y+1==factors[x]:
            numbers.append(counter)
            numbers.append(counter2)
total=0
for x in numbers:
    total+=x
print total
