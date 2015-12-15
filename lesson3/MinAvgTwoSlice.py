#!/usr/bin/env python


def solution(A):
    n = len(A)
    p = [0] * (n + 1)

    min_avg = 2 ** 31 - 1
    min_avg_i = 0
    for k in xrange(1, n + 1):
        p[k] = p[k - 1] + A[k - 1]

        if k > 1:
            avg = (p[k] - p[k - 2]) / 2.0
            if avg < min_avg:
                min_avg = avg
                min_avg_i = k - 2

        if k > 2:
            avg = (p[k] - p[k - 3]) / 3.0
            if avg < min_avg:
                min_avg = avg
                min_avg_i = k - 3

    return min_avg_i


def test():
    a = [4, 2, 2, 5, 1, 5, 8]
    assert solution(a) == 1


if __name__ == '__main__':
    test()
