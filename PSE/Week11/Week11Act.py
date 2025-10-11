
def add(a,b):

    '''
    Adds two numbers and returns the result.
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    1
    '''

    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(add(2,3))