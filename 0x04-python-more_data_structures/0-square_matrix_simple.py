#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = [[slot ** 2 for slot in row]for row in matrix]
    return squared
