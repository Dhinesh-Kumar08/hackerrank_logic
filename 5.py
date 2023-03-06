a1=int(input())
a2=int(input())
a3=int(input())

my_list=[a1,a2,a3]
print(my_list)
my_lists=[]
def list_operation(my_list):
    my_list.remove(6)
    my_lists.append(9)
    my_lists.append(1)
    my_list=my_list+my_lists
    print(sorted(my_list))
    my_list.remove(10)
    a = sorted(my_list)
    print(a[::-1])
    return my_lists
list_operation(my_list)