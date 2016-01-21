#!/usr/bin/env python


def solution(N, A):
    s = [0] * N
    max_ = base = 0
    for n in A:
        if 1 <= n <= N:
            if s[n-1] < base:
                s[n-1] = base + 1
            else:
                s[n-1] += 1
            if s[n-1] > max_:
                max_ = s[n-1]
        elif n == N + 1:
            base = max_

    for i, n in enumerate(s):
        if n < base:
            s[i] = base

    return s

if __name__ == '__main__':
    a = [3, 4, 4, 6, 1, 4, 4]
    print solution(5, a)
    a = [3, 4, 4, 6, 1, 4, 4, 6]
    print solution(5, a)
    a = [3]
    print solution(5, a)
