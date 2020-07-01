def Find_Fib(start1,start2,maxnumber):
    thingy=[start1,start2]
    while thingy[-1]<maxnumber:
        thingy.append(thingy[-1]+thingy[-2])
    return thingy[:-1]

def Even_Sum(sequence):
    total=0
    for x in sequence:
        if x%2==0:
            total+=x
    return total

print Even_Sum(Find_Fib(1,2,4000000))
