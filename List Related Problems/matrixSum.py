# Given a matrix of order m*n, the task is to find out the sum of each row and each column of a matrix. First create matrix with nested for loop and then sum of each row and each column by adding up the elements

row = 4  # defining number of rows
col = 4  # defining number of columns

# declaring a 2d list with values as 0
matrix = [[0 for c in range(col)]for r in range(row)]

for r in range(len(matrix)):
    for c in range(len(matrix)):
        print(matrix[r][c], end=" ")
    print()

# declaring a value to keep in the matrix
value = 1

# adding value to the matrix
for r in range(len(matrix)):
    for c in range(len(matrix)):
        matrix[r][c] += value
        value += 1
    print(matrix[r])

print()
# printing the sum of rows
for r in range(len(matrix)):
    sum = 0
    for c in range(len(matrix)):
        sum += matrix[r][c]
    print("Sum of row no.", r, 'is: ', matrix[r], "=", sum)

print()
# printing the sum of columns
for r in range(len(matrix)):
    sum = 0
    column = []
    for c in range(len(matrix)):
        sum += matrix[c][r]
        column.append(matrix[c][r])
    print("Sum of column no", r, "is: ", column, "=", sum)
