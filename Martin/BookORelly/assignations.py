#pylint:
#As your code is not contained in a class or function it is expecting
#those variables to be constants and as such they should be uppercase.


"""@package docstring
Assignation related to FOR cycles
+= =+ have different context.
"""

VAR_A = 1
print("VAR_A:", VAR_A)
VAR_B = VAR_A + 1
print("VAR_B=VAR_A+1:", VAR_B)
VAR_A += 1
print("VAR_A+=1:", VAR_A)
VAR_A = + 1
print("VAR_A=+1:", VAR_A)


def myfunction(arg1, arg2, kwarg='whatever.'):
    """
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    """
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)

#isinstance check method failure:
#print(myfunction("2", 23.5))
print(myfunction(2, 3))