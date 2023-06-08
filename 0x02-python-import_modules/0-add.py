#!/usr/bin/python3
import add_0

add = add_0.add

add_0.a = 1
add_0.b = 2

a = add_0.a
b = add_0.b
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

