#!/use/bin/python3
def common_elements(set_1, set_2):
    common_elem = []
    for x in set_1:
        if x in set_2:
            common_elem.append(x)
    return common_elem
