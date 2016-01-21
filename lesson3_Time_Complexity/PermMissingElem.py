#!/usr/bin/env python

def solution(A):
    n = len(A) + 1
    sum_ = n * (n + 1) / 2
    return sum_ - sum(A)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print solution(a)
    a = [1, 3]
    print solution(a)
    a = [1]
    print solution(a)
    a = []
    print solution(a)
