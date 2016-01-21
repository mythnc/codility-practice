#!/usr/bin/env python


def solution(S, P, Q):
    n = len(S)
    dna = "ACGT"
    dna_len = len(dna)
    p = [[0 for i in range(dna_len)] for j in range(n + 1)]

    for i in xrange(1, n + 1):
        pos = dna.index(S[i-1])

        for j in xrange(dna_len):
            p[i][j] = p[i - 1][j]

            if j == pos:
                p[i][j] += 1

    result = []
    for i in xrange(len(P)):
        head = P[i]
        tail = Q[i] + 1
        for j in xrange(dna_len):
            val = p[tail][j] - p[head][j]
            if val > 0:
                result.append(j + 1)
                break

    return result


def test():
    s = 'CAGCCTA'
    p = [2, 5, 0]
    q = [4, 5, 6]
    assert solution(s, p, q) == [2, 4, 1]


if __name__ == '__main__':
    test()
