def add_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if rows1 != rows2 or cols1 != cols2:
        print("\nMatrix addition is not possible as dimensions of matrices are not the same.")
        return None

    # Initialize ans matrix to be of dimensions rows1 x cols2 with all elements set to 0
    ans = [[0 for _ in range(cols1)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols1):
            ans[i][j] = mat1[i][j] + mat2[i][j]

    return ans

# Example matrices
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = add_matrices(mat1, mat2)

if result is not None:
    print("\nResultant Matrix 'ans' of dimension:", len(result), "X", len(result[0]), "is:")
    for row in result:
        row_str = ""
        for element in row:
            row_str += str(element) + " "
        print(row_str)
