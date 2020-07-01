def Find_Multiples(number,upperlimit):
    counter=1
    multiples=[number]
    while multiples[-1]<upperlimit:#
        counter+=1
        multiples.append(counter*number)
    return multiples[:-1]

a3=Find_Multiples(3,1000)
a5=Find_Multiples(5,1000)
total=0
for x in a3:
    total+=x
for x in a5:
    if x not in a3:
        total+=x
print total
