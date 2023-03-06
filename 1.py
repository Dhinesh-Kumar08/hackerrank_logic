'''Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird
#Input Format

#A single line containing a positive integer,n .

#Constraints
#1<n<100

#Output Format
#Print Weird if the number is weird.
Otherwise, print Not Weird.'''


n = int(input("enter the number"))
def fuction_number(n):
    if n % 2 != 0:
        print("Weird")
    elif(n % 2 == 0) & 2<=n<=5:
        print("Not Weird")
    elif(n % 2 == 0) & 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
fuction_number(n)
