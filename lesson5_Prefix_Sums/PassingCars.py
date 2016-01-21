#!/usr/bin/env python


def solution(A):
    sum_ = 0
    count = 0
    for i in reversed(A):
        if i == 0:
            sum_ += count
        elif i == 1:
            count += 1

    if sum_ > 1000000000:
        return -1
    return sum_


def test():
    a = [0, 1, 0, 1, 1]
    assert solution(a) == 5
    a = [0]
    assert solution(a) == 0
    a = [1]
    assert solution(a) == 0


if __name__ == '__main__':
    test()
