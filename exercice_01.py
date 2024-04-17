def resolve_one_loop(list, n):
    for i, elements in enumerate(list) :
        for j, secondelement in enumerate(list) :
            if elements + secondelement == n and i!=j:
                return True
    return False

ma_liste = [3, 2, 5, 1]
n = 8

resultat = resolve_one_loop(ma_liste, n)

print("Existe-t-il une paire qui somme à 8?", "Oui" if resultat else "Non")