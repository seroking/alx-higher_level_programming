#!/usr/bin/python3
import add_0 as add

add = add.add

add.a = 1
add.b = 2

a = add.a
b = add.b
print("{} + {} = {}".format(a, b, add(a, b)))
