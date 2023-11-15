def sparseMatrix(sparse, n):
    arr=[]

    count = 0

    arr.append([n,n,0])
    for i in range(n):
        for j in range(n):
            if sparse[i][j] !=0:
                arr.append([i,j,sparse[i][j]])
                count+= 1

    arr[0][2] = count
    return arr

compactMatrix = sparseMatrix([
    [5, 0 , 0, -5],
    [12, 4, 0, 0],
    [0, 0, -8, 0],
    [0, 0, 0, 0],
    [10, 0, 0, 0],
    [0, 45, 0, 0]

],4)


for i in range(len(compactMatrix)):
    print(compactMatrix[i])