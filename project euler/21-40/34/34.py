import math
total1=0
x=3
while x<100000:
    x+=1
    total=0
    for char in str(x):
        total+=math.factorial(int(char))
    if x==total:
        total1+=x
print total1
