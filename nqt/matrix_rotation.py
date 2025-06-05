


matrix = [[1,2,3],[4,5,6],[7,8,9]]


n = len(matrix)
new_matrix = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        new_matrix[j][n-i-1] = matrix[i][j]

print(new_matrix)