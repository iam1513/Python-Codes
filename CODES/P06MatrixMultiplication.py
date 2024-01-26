mat1 = [
    [1,2,3],
    [4,5,6],
    ]

mat2 = [
    [1,2],
    [4,5],
    [7,8]
    ]

rows1 = len(mat1)
cols1 = len(mat1[0])
rows2 = len(mat2)
cols2 = len(mat2[0])
print("\nMatrix 1 is of dimension :",rows1,"X",cols1)
print("\nMatrix 2 is of dimension :",rows2,"X",cols2)

if(cols1 != rows2):
    print("\n Multiplication is not possible. Number of colums in \
 Matrix 1 should be equal to number of rows of matrix 2")

else:
    # Initialize ans matrix to be of dimensions rows1 x cols2 with all elements set to 0
    ans = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(0,rows1):
        for j in range(0,cols2):
            for k in range(0,cols1):
                ans[i][j] += mat1[i][k] * mat2[k][j]

    print("\nResultant Matrix 'ans' of dimension :",rows1,"X",cols2," is :")

    for i in range(0,rows1):
        for j in range(0,cols2):
            print(ans[i][j],end=" ")
        print(" ")