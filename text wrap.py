a =str(input())
n = int(input())
arr = []
for i in range(len(a)):
    if i % n == 0:
        ts = i + n
        out =(a[i:ts])
        arr.append(out)
arr2 ="\n".join(arr)
print(arr2)
