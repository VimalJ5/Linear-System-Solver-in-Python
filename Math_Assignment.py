#------------------------------------------------------------------------------------------------

f = open("matrix.txt","r")
L = f.read().splitlines()

#------------------------------------------------------------------------------------------------

matrix = []
for i in L:
    P = []
    p = i.split()
    for i in p:
        P.append(float(i))
    matrix.append(P)
row = len(matrix)
column = len(matrix[0])

#--------------------------------------------------------------------------------------------------

def printmat(matrix,ends = " ",value = 4):
    for i in matrix:
        for j in i:
            print(j, end=" "*4)
        print()
def rowswap(matrix,r1,r2):
    matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
    return matrix

def scalarmult(matrix,r1,scalar):
    matrix[r1] = [round(scalar*i,5) for i in matrix[r1]]
    return matrix

def addsub(matrix,r1,r2,scalar):
    matrix[r1] = [matrix[r1][i] + scalar * matrix[r2][i] for i in range(len(matrix[r1]))]
    return matrix

def convertzero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -0.0:
                matrix[i][j] = 0.0
    return matrix

#-------------------------------------------------------------------------------------------------

print("\nOriginal Matrix:")
printmat(matrix)

if row<=column:
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[j][i] != 0:
                matrix = rowswap(matrix,i,j)
                break
        if matrix[i][i] != 0:
            for j in range(i+1, len(matrix)):
                matrix = addsub(matrix,j,i, -matrix[j][i]/matrix[i][i])
        try:
            for j in range(i-1, -1, -1):
                matrix = addsub(matrix,j, i, -matrix[j][i]/matrix[i][i])
        except ZeroDivisionError:
            pass
else:
    sub = row-column
    for i in range(len(matrix)-sub):
        for j in range(i, len(matrix)):
            if matrix[j][i] != 0:
                matrix = rowswap(matrix,i,j)
                break
        if matrix[i][i] != 0:
            for j in range(i+1, len(matrix)):
                matrix = addsub(matrix,j,i, -matrix[j][i]/matrix[i][i])
        try:
            for j in range(i-1, -1, -1):
                matrix = addsub(matrix,j, i, -matrix[j][i]/matrix[i][i])
        except ZeroDivisionError:
            pass
    pass

#----------------------------------------------------------------------------------------------------------
c = None
for i in matrix:
    for j in range(len(i)):
        if i[j] != 0:
            c=i[j]
            break
        
    if c != None:
        for k in range(len(i)):
            i[k] = round(i[k]/c,5)
            if i[k] == -0.0:
                i[k] = 0.0
#print()
#printmat(matrix)
matrix.sort(reverse=True)
#print()
#printmat(matrix)

#-----------------------------------------------------------------------------------------------------------

c = 0
d= {}
for i in range(len(matrix)-1,0,-1):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1.0:
            for k in range(i-1,0,-1):
                if matrix[k][j] == 0:
                    pass
                else:
                    for p in range(i-1, -1, -1):
                        try:
                            matrix = addsub(matrix,p, i, -matrix[p][i]/matrix[i][i])
                        except ZeroDivisionError:
                            pass
            if matrix[0][j] == 0:
                pass
            else:
                for p in range(i-1, -1, -1):
                    try:
                        matrix = addsub(matrix,p, i, -matrix[p][j])
                    except ZeroDivisionError:
                        pass
            break


print("\nRREF:")
printmat(matrix)

#----------------------------------------------------------------------------------------------------------------

pivot = []
orig_pivot = []
for i in matrix:
    for j in range(len(i)):
        if i[j] == 1.0:
            pivot.append(j)
            orig_pivot.append(j+1)
            break
#print()
#print(pivot)

fv=[]
orig_fv=[]
for i in matrix:
    for j in range(len(i)):
        if j not in pivot and j not in fv:
            fv.append(j)
            orig_fv.append(j+1)
#print(fv)

#-------------------------------------------------------------------------------------------------------------------

count = 0
colmat = []
for i in range(column):
    L = []
    for j in matrix:
        L.append(j[i])
    colmat.append(L)
#print("\nColumn Matrix:")
#printmat(colmat)

#--------------------------------------------------------------------------------------------------------------------

reformedcolmat = [[-j for j in i] for i in colmat]
reformedcolmat = convertzero(reformedcolmat)

#-----------------------------------------------------------------------------------------------------------

#SOLUTION

print("\nSolution:")
#print(matrix)
soldic = {}
for i in range(len(matrix)):
    if matrix[i] == [0]*column:
        pass
    else:
        tempdict = {}
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1.0 and j in pivot:
                key = "x"+str(j+1)
            #else:
            if j not in pivot:
                tempdict["x"+str(j+1)] = -(matrix[i][j])
        soldic[key] = tempdict

#print()
#print(soldic)

finaldic = {}
for (k1,v1) in soldic.items():
    for (k2,v2) in v1.items():
        if k2 not in list(finaldic.keys()):
            finaldic[k2] = [v2]
        else:
            finaldic[k2] += [v2]

#print()
#print(finaldic)

for (k,v) in finaldic.items():
    for j in fv:
        if k=="x"+str(j+1):
            finaldic[k].insert(j,1.0)
        else:
            finaldic[k].insert(j,0.0)


values = list(finaldic.values())
values = convertzero(values)
for index,(k,v) in enumerate(finaldic.items()):
    finaldic[k] = values[index]

if matrix == [[0]*column]*row:
    zerodic = {}
    for i in range(len(matrix[0])):
        templist = [0]*column
        templist[i] = 1
        zerodic["x"+str(i+1)] = templist
    x = ""
    print("\nx =",end = " ")
    for (k,v) in zerodic.items():
        x = x+("  "+k+"*"+str(v)+" + ")
    print(x[:len(x)-2:])

elif finaldic == {}:
    print("Trivial Solution, x = 0 for all x in R^"+str(column))
else:
    x = ""
    print("\nx =",end = " ")
    for (k,v) in finaldic.items():
        x = x+("  "+k+"*"+str(v)+" + ")
    print(x[:len(x)-2:])

#-------------------------------------------------------------------------------------------------------------