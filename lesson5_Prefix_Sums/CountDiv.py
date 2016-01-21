#!/usr/bin/env python


def solution(A, B, K):
    if A % K == 0:
        return B / K - A / K + 1
    return B / K - A / K


def test():
    assert solution(6, 11, 2) == 3
    assert solution(6, 12, 2) == 4
    assert solution(5, 11, 2) == 3
    assert solution(5, 12, 2) == 4
    assert solution(6, 11, 3) == 2


if __name__ == '__main__':
    test()
