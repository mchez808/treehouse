import math

def factorial(n):
    """
    >>> factorial(3)
    6

    >>> factorial(4)
    24

    >>> factorial(5)
    120
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("*"*20)
    print("Recall: if nothing is returned to the console, then there were zero errors in doctest.")
    print("*"*20)
