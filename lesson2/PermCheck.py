#!/usr/bin/env python

def solution(A):
    n = len(A)
    sum_ = sum(set(A))
    if sum_ == (n * (n + 1) / 2):
        return 1
    else:
        return 0

if __name__ == '__main__':
    a = [4, 1, 3, 2]
    print solution(a)
    a = [4, 1, 3]
    print solution(a)
    a = [4, 1, 1]
    print solution(a)
