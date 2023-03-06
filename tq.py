'''matrix_e=[[1,2,3],[4,5,6]]
matrix_2=[]
for arr in matrix_e:
    arr2 =[]
    for item in arr :
        arr2.append(item+1)
    matrix_2.append(arr2)
print(matrix_2)
ppp
'''
n = int(input())
def adding(n):
    matrix = []
    for i in range(1,n+1):
        if i % 2 == 0:
            matrix.append(i)
        else:
            pass
    return matrix
output = adding(n)
print(output)