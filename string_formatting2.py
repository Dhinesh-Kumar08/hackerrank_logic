a = str(input())
b = str(input())
count = 0
print(a[2:2+3])

for i in range(len(a)):
    if str(a[i:i+len(b)]) == b:
            count = count + 1
print(count)

if __name__ == '__main__':
    print(count)