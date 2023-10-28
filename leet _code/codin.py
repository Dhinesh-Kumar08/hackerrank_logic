a ="i love country india"
b=""
c=""
e=hash(a)
d=[]
f=[]
for i in a:
    if i == e:
        b = b+i
    else:
        c=b
        d.append(c)
        b=""
d.append(b)
print(b)