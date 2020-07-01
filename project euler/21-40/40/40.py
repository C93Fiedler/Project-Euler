d=[]
x=0
counter=0
flag1=True
flag10=True
flag100=True
flag1000=True
flag10000=True
flag100000=True
flag1000000=True
while counter<1000000:
    x+=1
    if flag1:
        if counter+len(str(x))>=1:
            flag1=False
            d.append(int(str(x)[1-counter-1]))
            print d
    elif flag10:
        if counter+len(str(x))>=10:
            flag10=False
            d.append(int(str(x)[10-counter-1]))
            print d
    elif flag100:
        if counter+len(str(x))>=100:
            flag100=False
            d.append(int(str(x)[100-counter-1]))
            print d
    elif flag1000:
        if counter+len(str(x))>=1000:
            flag1000=False
            d.append(int(str(x)[1000-counter-1]))
            print d
    elif flag10000:
        if counter+len(str(x))>=10000:
            flag10000=False
            d.append(int(str(x)[10000-counter-1]))
            print d
    elif flag100000:
        if counter+len(str(x))>=100000:
            flag100000=False
            d.append(int(str(x)[100000-counter-1]))
            print d
    elif flag1000000:
        if counter+len(str(x))>=1000000:
            flag1000000=False
            d.append(int(str(x)[1000000-counter-1]))
    counter+=len(str(x))
print d
