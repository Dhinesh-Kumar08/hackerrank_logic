'''https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true'''

string = str(input())
s = list(string)
i,c = input().split()
s[i] = c
string =''.join(s)
print(string)