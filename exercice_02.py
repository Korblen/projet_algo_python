def resolve_two_loops(list):
    result = []
    for i, elements in enumerate(list):
        for j, secondelement in enumerate(list):
            if j>i and secondelement > elements :
                break
        else:
            result.append(elements)
    return len(result)

numbers_list = [3, 7, 4, 6, 5, 1]

result = resolve_two_loops(numbers_list)
print("Liste des éléments non suivis par un élément supérieur :", result)