limit=6*9**5
cunt=[]
for x in range(100,limit):
    summ=0
    for char in str(x):
        summ+=int(char)**5
    if summ==x:
        cunt.append(x)
print sum(cunt)
