#this problem is shit, "trivial" is poorly defined
from __future__ import division
xs=[]
ys=[]
cunt=[]
for x in range(11,100):
    for y in range(x+1,100):
        try:
            if x/y==int(str(x)[0])/int(str(y)[1]):
                xs.append(x)
                ys.append(y)
            elif x/y==int(str(x)[1])/int(str(y)[0]):
                cunt.append(x/y)
        except Exception:
            pass
print cunt
print xs
print ys
