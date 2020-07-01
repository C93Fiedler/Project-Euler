#1
def Find_Multiples(number,upperlimit):
    counter=1
    multiples=[number]
    while multiples[-1]<upperlimit:#
        counter+=1
        multiples.append(counter*number)
    return multiples[:-1]

#2
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

#3
def Is_Prime(number):
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

def Prime_Factors(number):
    #assuming number is not even
    factors=[]
    counter=1
    while number!=1:
        counter+=2
        if Is_Prime(counter):
            if number%counter==0:
                factors.append(counter)
                number/=counter
                counter=1

#6
def Sum(n,lim):
    total=0
    for x in range(1,lim+1):
        total+=x**n
    return total

#12
def Factors(number):
    factors=[1]
    counter=1
    limit=number**0.5
    while counter<limit:
        counter+=1
        if number%counter==0:
            factors.append(counter)     
    return factors+factors

#23
def Factors(number):
    factors=[1]
    counter=1
    limit=number/2
    while counter<limit:
        counter+=1
        if number%counter==0:
            factors.append(counter)     
    return factors

#37
def Is_Prime(number):
    if number==1:
        return False
    if number==2:
        return True
    for x in range(2, int((number)**0.5)+2):
        if number%x==0:
            return False
    return True

#42
def Is_Triangular(word):
    global letters
    total=0
    for char in word:
        total+=letters[char]
    n=0.5*((1+8*total)**0.5-1)
    if int(n)==n:
        return True
    return False

def Load_File():
    data=''
    thefile=open('p042_words.txt', "r")
    for line in thefile:
        data=data+line
    thefile.close()
    data=data.split(',')
    return data

#45
def Is_Pentagonal(x):
    n=(1+(1+24*x)**0.5)/6
    if n==int(n):
        return True
    return False

def Is_Hexagonal(x):
    n=(1+(1+8*x)**0.5)/4
    if n==int(n):
        return True
    return False
