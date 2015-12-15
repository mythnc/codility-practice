#!/usr/bin/env python
import bisect


def solution(A):
    n = len(A)
    ary = [[0 for i in range(2)] for j in range(n)]

    for i in xrange(n):
        ary[i][0] = i - A[i]
        ary[i][1] = i + A[i]

    ary.sort(key=lambda x: x[0])

    sum_ = 0
    left_part = [i[0] for i in ary]
    for i in xrange(n):
        right_value = ary[i][1]
        pos = bisect.bisect(left_part, right_value, lo=i)
        sum_ += (pos - i - 1)

    if sum_ > 10000000:
        return -1
    return sum_


def test():
    a = [1, 5, 2, 1, 4, 0]
    assert solution(a) == 11


if __name__ == '__main__':
    test()
