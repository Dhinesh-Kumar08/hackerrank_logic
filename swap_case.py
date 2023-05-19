
'''https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true'''

a = "Hello World"
b = 'qwertyuiopasdfghjklzxcvbnm'
c = "QWERTYUIOPASDFGHJKLZXCVBNM"
d=""
for i in a:
    if i in b:
        l =i.upper()
        d=d+l
        
    elif i in c:
        h =i.lower()
        d = d+h
print(d)