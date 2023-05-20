a = str(input())
sav = []
arr = (a.split(" "))
print(arr)
for i in arr:
    out = i.capitalize()
    sav.append(out)
arr2 = (" ").join(sav)
print(arr2)