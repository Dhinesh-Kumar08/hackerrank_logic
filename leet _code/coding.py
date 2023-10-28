'''a = list(map(int,input().split()))
cout = 0
for i in a:
    cout = cout + i
print(cout)'''

a = list(input())
a = a.remove("''")
print(a)
for i in a:
    if i == str:
        print(str(i))
    elif i == int:
        print(int(i))
    elif i == float:
        print(float(i))