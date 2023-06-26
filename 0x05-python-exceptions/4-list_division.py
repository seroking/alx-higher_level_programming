#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for idx in range(0, list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
        finally:
            div_list.append(result)
    return (div_list)
