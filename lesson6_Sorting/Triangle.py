#!/usr/bin/env python


def solution(A):
    A.sort()

    for i in xrange(len(A) - 1, 1, -1):
        if A[i - 1] + A[i - 2] > A[i]:
            return 1
    return 0


def test():
    a = [10, 2, 5, 1, 8, 20]
    assert solution(a) == 1


if __name__ == '__main__':
    test()
