n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
n6=int(input())
def maxof(n1,n2,n3,n4,n5,n6):
    list1=(list(n1,n2,n3,n4,n5,n6))
    n=int(input())
    maximum=max(list1)-1
    if n==maximum:
        print(maximum)
