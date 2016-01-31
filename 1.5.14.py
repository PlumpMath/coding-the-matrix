# coding=utf-8
# Task 1.5.14

S = {-4, -2, 1, 2, 5, 0}

result = [
    (i, j, k)
    for i in S
    for j in S
    for k in S
    if (0 == (i + j + k))
]

print (result)

