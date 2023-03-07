'''you are given three intgers x,y and z represting the dimensions of a cuboid along with an integer n
print a list of all posibble coordinates givenn by (i,j,k) on a 3d grid where the sum of i+j+k is not
equal to n .here 0<=i<=x;0<=j<=y;0<=k<=z.
sample input:
x=1
y=1
z=2
n=3
sample output
[[000],[001],[010],[100],[111]]
'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
# Using list comprehension

def list_comprehension(x,y,z,n):
    newlist = [[i,j,k]
    for i in range(x+1) 
    for j in range(y+1)
    for k in range(z+1)
        if (i+j+k) !=n]
    print(newlist)
    
