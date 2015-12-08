#!/usr/bin/env python
import math

def solution(X, Y, D):
    return int(math.ceil((Y - X) * 1.0 / D))


if __name__ == '__main__':
    print solution(10, 85, 30)
    print solution(10, 70, 30)
    print solution(10, 10, 30)
    
