#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        for i in range(len(tuple_a)):
            if not tuple_a[i]:
                tuple_a[i] = 0
        for j in range(len(tuple_b)):
            if not tuple_b[j]:
                tuple_b[j] = 0

        result = []
        for i in range(min(len(tuple_a), len(tuple_b))):
            add = tuple_a[i] + tuple_b[i]
            result.append(add)

        return tuple(result)
