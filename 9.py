
'''
FIND THE RUNNER UP SCORE
input format
the first line contain n the second line contain an array A[] of n integers each separated by a space.

constraints
->2<=n<=10
->-100<=a[i]<=100
output format 
print the runner up score

sample input
5
2 3 6 6 5

sample output
5


explaination
given list is [2,3,6,6,5].that  maximum value of list is 6
the runner is the logic minus of maximum then print the 
value
'''










n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
n6=int(input())
def maxof(n1,n2,n3,n4,n5,n6):
    a=[]
    list1=(list(n1,n2,n3,n4,n5,n6))
    n=int(input())
    maximum=max(list1)-1
    return maximum
maxof(n1,n2,n3,n4,n5,n6)

