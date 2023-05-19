'''You are given a string.
Split the string on a " " (space) delimiter and join using a - hyphen.
input format
this is string

output format
this-is-string'''
a = input()
def split_join(a):
    A = a.split(" ")
    output = "-".join(A)
    return output
print(split_join(a))