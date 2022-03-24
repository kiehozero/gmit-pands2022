# a module of useful functions

def factorial(num):
    """ function that returns the factorial number of a integer,
    i.e. 7x6x5x4x3x2x1=5040 """
    if num == 1:
        return 1
    factorial = 1
    num += 1
    for i in range(1,num):
        factorial *= i
    return factorial

if __name__ == "__main__":
    print("this is run directly")
    assert factorial(7) == 5040