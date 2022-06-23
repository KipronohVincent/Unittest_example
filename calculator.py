#!/usr/bin/python3
def add(x, y):
    """addition"""
    return x + y


def sub(x, y):
    """subtraction"""
    return x - y  

def mul(x, y):
    """multiplication"""
    return x * y

def div(x, y):
    """division"""
    if y == 0:
        raise ValueError('Not divisible by zero')
    return x / y
            