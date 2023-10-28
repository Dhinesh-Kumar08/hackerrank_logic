a =[]
b =""
n = int(input())
for i in range(n):
    i = str(input())
    a.append(i)
print(a)
v = sorted(a)
print(v)
first = a[0]
last = a[-1]
print(first,last)
for i in range(min(len(first),len(last))):
    if (first[i]!=last[i]):
        pass