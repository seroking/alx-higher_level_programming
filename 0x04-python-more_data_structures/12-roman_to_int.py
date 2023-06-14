#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs = [roman_dict[i] for i in roman_string]
    result = 0
    for j in range(len(decs)):
        result += decs[j]
        if decs[j - 1] < decs[j] and j != 0:
            result -= (decs[j - 1] + decs[j - 1])
    return result
