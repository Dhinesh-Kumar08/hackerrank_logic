def number(a):
    b=["zero","one","two","three","four","five","six","seven","eight","nine"]
    c=[]
    d=["triple zero","triple one","triple two","triple three","triple four","triple five","triple six","triple seven","triple eight","triple nine"]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(j)
            elif a[i][0] == "d":
                e=(a[i][7:])
                if e in b:
                    for k in range(len(b)):
                        if e == b[k]:
                            c.append(k)
                            c.append(k)
                            break
                    break
            elif a[i] in d:
                f=a[i][7:]
                if f in b:
                    for l in range(len(b)):
                        if f == b[l]:
                            c.append(l)
                            c.append(l)
                            c.append(l)
                            break
                    break 
    print(*c)                
a=["eight","nine","five","double four","triple zero","three","nine","double nine"]
print(number(a))
