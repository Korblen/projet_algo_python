def resolve_two_n(list):
    result = []
    max_seen = 0
    for elements in reversed(list):
        if elements > max_seen:
            max_seen = elements
            result.append(elements)
    return len(result)