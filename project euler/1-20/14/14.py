def Collatz(number):  
    if number%2==0:
        return number/2
    return 3*number+1

counter=1
longest=0
while counter<1000000:
    counter+=1
    chaincounter=1
    number=counter
    while number!=1:
        chaincounter+=1
        number=Collatz(number)
    if chaincounter>int(longest):
        longest=str(chaincounter)
        print str(counter)+", " +longest
