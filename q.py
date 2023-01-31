#Reading the size of the matrix
f = open("matrix.txt","r")
L = f.read().splitlines()
size = [int(i.split(": ")[1]) for i in L[0].split(", ")]
row,column = size[0],size[1]
#print(size)

#Reading the matrix
matrix = []
for i in L[1::]:
    P = []
    p = i.split()
    for i in p:
        P.append(int(i))
    matrix.append(P)
print(matrix)

def scalarmult(matrix,k,r):
    l = len(L[row])
    for i in range(l):
        matrix[r][i] = k*matrix[r][i]
    return matrix

def interchange(matrix,r1,r2):
    matrix[r1],matrix[r2] = matrix[r2],matrix[r1]
    return matrix

def rowop(matrix,r1,r2,k):
    l = len(matrix[row])
    for i in range(l):
        matrix[r1][i] = matrix[r1][i] + k*(matrix[r2][i])
    return matrix
