#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1,'X': 10,  'L': 50, 'C': 100, 'D': 500,'M': 1000}
    if roman_string is not str or roman_string is None:
        return 0

    decs = [roman_num[x] for x in roman_string]

    num = 0

    for i in range(decs):
        num  += decs[i]
        if decs[i - 1] < decs[i] and i != 0:
            num -= (decs[i - 1] + decs[i - 1])
    return num
