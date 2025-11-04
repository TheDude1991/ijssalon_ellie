def mijn_functie_1(argument):
    mapping = {
        2 : 4,
        4 : 16,
        10 : 100,
        12 : 144
    }
    return mapping.get(argument)

print(mijn_functie_1(2))

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a//b)
    return uitvoer_lijst

print(mijn_functie_2(12, 3))
