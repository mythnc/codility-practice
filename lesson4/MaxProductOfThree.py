#!/usr/bin/env python


def solution(A):
    A.sort()

    case1 = A[0] * A[1] * A[-1]
    case2 = A[-1] * A[-2] * A[-3]

    if case1 > case2:
        return case1
    return case2


def test():
    a = [-3, 1, 2, -2, 5, 6]
    assert solution(a) == 60


if __name__ == '__main__':
    test()
