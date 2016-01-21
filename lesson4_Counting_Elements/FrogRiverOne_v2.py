#!/usr/bin/env python

def solution(X, A):
    table = [0] * X
    count = 0
    for i, leaf in enumerate(A):
        if table[leaf-1] == 0:
            table[leaf-1] = 1
            count += 1
        if count == X:
            return i
    return -1

if __name__ == '__main__':
    a = [1, 3, 1, 4, 2, 3, 5, 4]
    print solution(5, a)
    a = [1]
    print solution(1, a)
    a = [1, 3]
    print solution(3, a)
    a = [1]
    print solution(1, a)
    a = [1, 3, 1, 3, 2, 1, 3]
    print solution(3, a)
