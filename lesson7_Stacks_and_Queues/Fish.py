#!/usr/bin/env python


def solution(A, B):
    stack = []

    for size, flow in zip(A, B):
        while len(stack) > 0 and stack[-1][1] > flow:
            if stack[-1][0] < size:
                stack.pop()
            else:
                break

        if len(stack) == 0 or not stack[-1][1] > flow:
            stack.append([size, flow])

    return len(stack)


def test():
    A = [4, 3, 2, 1, 5]
    B = [0, 1, 0, 0, 0]
    assert solution(A, B) == 2


if __name__ == '__main__':
    test()
