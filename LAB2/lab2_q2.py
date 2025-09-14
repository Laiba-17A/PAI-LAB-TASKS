def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Cannot do addition."

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Cannot do multiplication."

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result

A = [
    [1, 2],
    [4, 5]
]

B = [
    [7, 8],
    [10, 1]
]
print("A + B =")
add_result = matrix_add(A, B)
for row in add_result:
    print(row)

print("\nA x B")
mul_result = matrix_multiply(A, B)
for row in mul_result:
    print(row)
