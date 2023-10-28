a = "abca"
a = list(a)
c=[]
for i in a:
    b =a.remove(i)
    c = b
    if a[::-1] == a:
        print("y")
    else:
        print("no")
    
