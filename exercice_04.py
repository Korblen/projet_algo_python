def resolve_two_n(list):
    result = []
    max_seen = 0
    for elements in reversed(list):
        if elements > max_seen:
            max_seen = elements
            result.append(elements)
    return len(result)

numbers_list = [3, 7, 4, 6, 5, 1]

result = resolve_two_n(numbers_list)
print("Liste des éléments non suivis par un élément supérieur :", result)