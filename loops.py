#The provided code stub reads and integer,n, from STDIN. For all non-negative integers ,i<n print i square.
#n=4
#0
#1
#4
#9



n=int(input("enter the needed square till this number  :"))
def square_root(n):
    for n in range(1,n+1):
        i=n*n
        print(i,end=" ")
    return i
square_root(n)