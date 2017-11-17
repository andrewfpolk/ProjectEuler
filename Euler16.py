#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:06:03 2017

@author: Polk
"""

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def powers(x,y):
    '''
    x and y are integers
    
    Returns x to the yth power
    *** Example: powers(2,15) returns the value 32768
    '''
    num = 1
    total = x
    while num < y:
        total = x*total
        num = num + 1
    return total

def sumofdigits(x):
    '''
    x is an intenger
    
    Returns the sum of the digits of x
    *** Example: sumofdigits(12345) returns the value 15
    '''
    alist = []
    string = str(x)
    answer = 0
    for char in string:
        alist.append(int(char))
    for n in alist:
        answer = answer + n
    return answer
    
print(sumofdigits(powers(2,1000)))