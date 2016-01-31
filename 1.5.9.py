# coding=utf-8
# Task 1.5.9

S = {1, 2, 3, 4}
T = {3, 4, 5, 6}

intersection = {
    s
    for s in S
    for t in T
    if s == t
}

print (intersection)


