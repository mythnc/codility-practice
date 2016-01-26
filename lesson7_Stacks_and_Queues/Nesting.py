#!/usr/bin/env python


def solution(S):
    stack = []

    for char in S:
        if char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return 0
        if char == '(':
            stack.append(char)

    if len(stack) != 0:
        return 0
    return 1


def test():
    s = '(()(())())'
    assert solution(s) == 1
    s = '())'
    assert solution(s) == 0


if __name__ == '__main__':
    test()
