#2d-list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[1][1])  # Output: 5

matrix[0][2] = 15
print(matrix)

for row in matrix:
    for item in row:
        print(item)
