#!/usr/bin/env python

def solution(A):
    n = len(A)
    head = sum(A)
    tail = 0
    min_ = 2 ** 31 - 1
    for i in range(n-1, 0, -1):
        tail += A[i]
        head -= A[i]
        diff = abs(head - tail)
        if diff < min_:
            min_ = diff
    return min_


if __name__ == '__main__':
    a = [3, 1, 2, 4, 3]
    print solution(a)
    a = [3, 4, 2, 1, 3]
    print solution(a)
    a = [3, -4, 2, 1, 3]
    print solution(a)
