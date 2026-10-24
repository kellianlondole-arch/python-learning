import sys
def matmult(A,B,l,m,n):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(l):
        for k in range (n):
            for j in range (m):
                C[i][k]=C[i][k]+A[i][j]*B[j][k]
    return print(C)

MATRIX1 = [[3, 2, 5], [1, 0, 0], [0, 1, 2]]
MATRIX2 = [[0, 1, 0], [2, 3, -1], [0, 0, 1]]


matmult(MATRIX1,MATRIX2,3,3,3)

def transpose(list):
    new_list=[[0 for i in range(len(list))]for j in range(len(list[0]))]
    for i in range(len(list)):#2 Zeilen
        for j in range (len(list[0])):#3 Spalten
            new_list[j][i] = list[i][j]

    return new_list


Matrix = [ [1,2,3],[4,5,6]]
Test = [[0 for i in range(2)]for j in range(3)]
print(transpose(Matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Soll zurückgeben: [1, 5, 9]

def diagonale(list):
    nl=[]
    for i in range (len(list)):
        for j in range (len(list[0])):

            if j == i :

                nl = nl+ [ list[i][j] ]
    return nl


print(diagonale(matrix))

def nextdiagonal(list):
    nl = []
    for i in range(len(list)):
        for j in range(len(list[0])):

            if j + i ==len(list)-1:

                nl = nl + [list[i][j]]
    return nl

matrix2 = [
    [1, 2, 3],  # braucht die 3 (Index [0][2])
    [4, 5, 6],  # braucht die 5 (Index [1][1])
    [7, 8, 9]   # braucht die 7 (Index [2][0])
]

# Soll zurückgeben: [3, 5, 7]
print(nextdiagonal(matrix2))