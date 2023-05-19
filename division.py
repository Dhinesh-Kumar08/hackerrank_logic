'''The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines.
The first line should contain the result of integer division, a //b .
The second line should contain the result of float division, a /b .'''
a = int(input())
b = int(input())
intdiv = a//b
fltdiv = a/b
print(intdiv,"\n",fltdiv)
'''sample input
3
5
sample output
0
0.6
'''