def m(n,matrix):
    for j in range(n):
        for i in range(n):
            print(matrix[i][j],end=" ")
        print()
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
m(n,matrix)
