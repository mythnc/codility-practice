#!/usr/bin/env python


def solution(A, K):
    n = len(A)
    if n == 0:
        return A

    K %= n
    if K == 0:
        return A
    return A[-K:] + A[:n-K]


def test():
    a = [3, 8, 9, 7, 6]
    assert solution(a, 1) == [6, 3, 8, 9, 7]
    assert solution(a, 6) == [6, 3, 8, 9, 7]
    assert solution(a, 3) == [9, 7, 6, 3, 8]
    assert solution(a, 0) == a


if __name__ == '__main__':
    test()
