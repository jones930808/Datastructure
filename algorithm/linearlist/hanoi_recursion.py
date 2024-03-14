#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : time : 2024/3/14


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C' )