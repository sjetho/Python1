# a = [2,4,5]
# b = [2,3,6]
# x = [a * b for a, b in zip(a, b)]
# print(x)

a = [[2, -2], [5, 3]]
b = [[2, -2], [5, 3]]
result = [[0,0], [0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]

for r in result:
    print(r)


