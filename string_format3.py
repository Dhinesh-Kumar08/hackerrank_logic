n = int(input())
for i in range(1,n+1):
    a = i
    b = bin(i)
    c = oct(i)
    d = hex(i)
    result = ("{}  {}   {}   {}".format(a,b,c,d))
    Result = result.replace("0b","").replace("0o","").replace("0x","")
    print(Result)

