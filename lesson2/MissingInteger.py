#!/usr/bin/env python

def solution(A):
    n = len(A)
    table = [0] * n

    for i in A:
        if 0 < i <= n:
            table[i-1] = 1

    for i, v in enumerate(table):
        if v == 0:
            return i + 1
    return n + 1


if __name__ == '__main__':
    a = [1, 3, 6, 4, 1, 2]
    print solution(a)
    a = [1]
    print solution(a)
    a = [4, 5, 6, 2]
    print solution(a)
