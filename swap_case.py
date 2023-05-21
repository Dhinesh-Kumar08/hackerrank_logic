a =input()
arr = []
for i in a:
    if i.isupper():
        odd =i.lower()
        arr.append(odd)
    elif i.islower():
        odd2 = i.upper()
        arr.append(odd2)
    else:
        arr.append(i)
arr2 ="".join(arr)
print(arr2)
