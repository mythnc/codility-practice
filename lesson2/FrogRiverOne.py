#!/usr/bin/env python

def solution(X, A):
    s = set()
    for i, leaf in enumerate(A):
        s.add(leaf)
        if len(s) == X:
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
