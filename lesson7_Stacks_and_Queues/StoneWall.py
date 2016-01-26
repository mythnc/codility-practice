#!/usr/bin/env python


def solution(B):
    stack = []
    count = 0

    for h in B:
        while len(stack) > 0 and h < stack[-1]:
            stack.pop()
            count += 1

        if len(stack) == 0 or h > stack[-1]:
            stack.append(h)

    return count + len(stack)


def test():
    h = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    assert solution(h) == 7


if __name__ == '__main__':
    test()

