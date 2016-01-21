#!/usr/bin/env python


def solution(N):
    max_gap = gap = 0
    for d in bin(N)[2:]:
        if d == '0':
            gap += 1
        elif d == '1':
            if max_gap < gap:
                max_gap = gap
            gap = 0

    return max_gap


def test():
    assert 5 == solution(1041)
    assert 2 == solution(9)
    assert 4 == solution(529)
    assert 1 == solution(20)
    assert 0 == solution(15)


if __name__ == '__main__':
    test()
