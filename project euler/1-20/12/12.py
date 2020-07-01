def Factors(number):
    factors=[1]
    counter=1
    limit=number**0.5
    while counter<limit:
        counter+=1
        if number%counter==0:
            factors.append(counter)     
    return factors+factors

counter=10
flag=True
while flag:
    counter+=1
    if len(Factors(counter*(counter+1)/2))>500:
        flag=False
print counter*(counter+1)/2
