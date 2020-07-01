fib=[0,1,1]
limit=10**999
counter=2
while fib[-1]<limit:
    counter+=1
    fib=fib[1:]
    fib.append(sum(fib))
print counter
