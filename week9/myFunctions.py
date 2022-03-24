# a module of useful functions

import logging as l

l.basicConfig(level=l.DEBUG)

def factorial(num):
    """ function that returns the factorial number of a integer,
    i.e. 7x6x5x4x3x2x1=5040 """
    if num < 0:
        l.warn("received a number below zero")
        return -1
    if num == 1:
        return 1
    factorial = 1
    num += 1
    for i in range(1,num):
        l.debug("before mult %s by %d", factorial, i)
        factorial *= i
        l.debug("after mult %s ", factorial)
    return factorial

if __name__ == "__main__":
    assert factorial(7) == 5040
    print("this is run directly")