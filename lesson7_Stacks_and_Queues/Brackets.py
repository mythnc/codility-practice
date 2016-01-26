#!/usr/bin/env python


def solution(S):
    stack = []
    left_symbols = ['(', '{', '[']
    right_symbols = [')', '}', ']']

    for char in S:
        if char in right_symbols:
            i = right_symbols.index(char)
            if len(stack) > 0 and stack[-1] == left_symbols[i]:
                stack.pop()
            else:
                return 0
        elif char in left_symbols:
            stack.append(char)

    if len(stack) != 0:
        return 0
    return 1


def test():
    s = '{[()()]}'
    assert solution(s) == 1
    s = '([)()]'
    assert solution(s) == 0
    assert solution('') == 1


if __name__ == '__main__':
    test()
