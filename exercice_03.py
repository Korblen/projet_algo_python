def resolve_one_n(list, n):
    seen = []
    for elements in list:
        result = n - elements
        if result in seen :
            return True
        else :
            seen.append(elements)
    return False

ma_liste = [3, 2, 1, 1, 4, 5]
n = 8

resultat = resolve_one_n(ma_liste, n)

print("Existe-t-il une paire qui somme à 8?", "Oui" if resultat else "Non")