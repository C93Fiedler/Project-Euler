total=0
for x in range(1,1000000):
    if str(x)==str(x)[::-1]:
        if str(bin(x)[2:])==str(bin(x)[2:])[::-1]:
            total+=x
print total
