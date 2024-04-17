def resolve_one_n(list, n):
    seen = []
    for elements in list:
        result = n - elements
        if result in seen :
            return True
        else :
            seen.append(elements)
    return False