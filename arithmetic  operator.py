#addtion of two number
#subraction of two number
#multiple of two number      



a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
def aritmetic_oper(a,b):
    print("adding of {} and {} is {}".format(a,b,a+b))
    print("subracting of {} and {} is {}".format(a,b,a-b))
    print("multiplication of {} and {} is {}".format(a,b,a*b))
    print("division of {} and {} is {}".format(a,b,a/b))
    print("modlus of {} and {} is".format(a,b,a%b))
    print("power of {} and {} is {}".format(a,b,a**b))
aritmetic_oper(a,b)