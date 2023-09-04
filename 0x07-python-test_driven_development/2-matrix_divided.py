#!/usr/bin/python3
"""
    module : 2-matrix_divided.py

"""
def matrix_divided(matrix, div):
    """
    divid all element of a matrix by 'div'

    args:
        matrix : list of a lists of numbers (float, int)
        div : divisor of all element of the matrix

    return:
       new_matrix
    """

    new_matrix = []
    size = 0

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if size != 0 and len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        if not row or not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for slot in row:
            if type(slot) not in [int or float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        size = len(row)

    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (n)
