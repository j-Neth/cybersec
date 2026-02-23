def dirOnly(instanza):
    metodi = dir(instanza)
    risultato = []
    for m in metodi:
        if not m.startswith("_"):
            risultato.append(m)
    return risultato

def discount(prices, isPet, nItems):
    risultato = 0.0
    base_sconto = 0.0
    numero_animali = 0
    if len(set(isPet)) == 2:
        index = 0
        for value in isPet:
            if value:
                numero_animali = numero_animali + 1
            else:
                base_sconto = base_sconto + prices[index]
            index = index + 1
        if (nItems - numero_animali) >= 5:
            risultato = base_sconto * 0.2
    return risultato

def main():
    prices = []
    isPet = []
    sconto = 0.0
    with open("lista.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split()
            prices.append(float(parts[0]))
            if parts[1].upper() == "Y":
                isPet.append(True)
            else:
                isPet.append(False)

    nItems = len(prices)
    if nItems == len(isPet):
        sconto = discount(prices, isPet, nItems)
        print("sconto totale", sconto)

if __name__ == "__main__":
    main()