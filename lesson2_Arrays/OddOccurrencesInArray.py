#!/usr/bin/env python


def solution(A):
    single = A[0]
    for n in A[1:]:
        single ^= n
    return single


def test():
    a = [9, 3, 9, 3, 9, 7, 9]
    assert 7 == solution(a)


if __name__ == '__main__':
    test()
