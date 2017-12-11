#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Assignment"""


def fibonacci(n):

    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    while b:
        (a, b) = (b, (a % b))
        return a


def stringcomparison(s1, s2):

    if len(s1) < len(s2):
        return len(s1) - len(s2)
    if len(s1) > len(s2):
        return len(s1) - len(s2)
    if len(s1) == len(s2):
        return 0
