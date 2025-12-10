def vytvor_pole(velikost):
    """fce vytvoří 2D hraci pole o velikosti """
    hraci_plocha = []
    for i in range(velikost):
        radek = []
        for y in range(velikost):
            radek.append(" ")
        hraci_plocha.append(radek)
    return hraci_plocha

def vykresli_hraci_plochu(hraci_plocha):
    """

    vykreslí pole o velikosti len(hraci_plocha)
    """
    velikost = len(hraci_plocha)
    vystup = "  " + " ".join(str(i+1) for i in range(velikost)) + "\n"
    for y in range(velikost):
        radek = f"{y + 1} " + " ".join(hraci_plocha[y]) + "\n"
        vystup  += radek
    print(vystup)

def tah_hrace(hraci_plocha, hrac):
    """

    """
    while True:

        x_str = input("Zadej pozici X kam chceš táhnout: ")
        y_str = input("Zadej pozici Y kam chceš táhnout: ")

        if not x_str.isdigit() and y_str.isdigit():
            print("Zadej prosím celé číslo.")
            continue

        x = int(x_str)
        y = int(y_str)

        if 1 <= x <= len(hraci_plocha) and 1 <= y <= len(hraci_plocha):
            if hraci_plocha[y-1][x-1] != " ":
                print("Neplatná pozice, zadej ji prosím znovu.")


            else:
                hraci_plocha[y - 1][x - 1] = hrac
                break
        else:
            print("Neplatná pozice, zadej ji prosím znovu.")



def kontrola_vyhry(hraci_plocha):

    for radek in hraci_plocha:
        # Kontrola výhry v řádku
        retezec_radku = "".join(radek)
        if "XXXXX" in retezec_radku:
            return "X"

        if "OOOOO" in retezec_radku:

            return "O"

    for sloupec in range(len(hraci_plocha)):
        # Kontrola výhry ve sloupci
        symboly = []
        for radek in range(len(hraci_plocha)):
            symboly.append(hraci_plocha[radek][sloupec])
        retezec_sloupce = "".join(symboly)
        if "XXXXX" in retezec_sloupce:

            return "X"
        if "OOOOO" in retezec_sloupce:

            return "O"

    horni_hrana = []
    leva_hrana = []

    for i in range(len(hraci_plocha)):
        horni_hrana.append((0,i))
        if i == 0:
            continue
        leva_hrana.append((i,0))


    for x , y in horni_hrana:
        # Kontrola výhry diagonálně horní hrany směrem dolů
        symboly = []
        while x < len(hraci_plocha) and y < len(hraci_plocha):
            symboly.append(hraci_plocha[x][y])
            x += 1
            y += 1
            if "XXXXX" in "".join(symboly):

                return "X"
            if "OOOOO" in "".join(symboly):

                return "O"

    for x , y in leva_hrana:
        # Kontrola výhry diagonálně levé hrany směrem dolů
        symboly = []
        while x < len(hraci_plocha) and y < len(hraci_plocha):
            symboly.append(hraci_plocha[x][y])
            x += 1
            y += 1
            if "XXXXX" in "".join(symboly):
                return "X"
            if "OOOOO" in "".join(symboly):

                return "O"


    horni_strana = []
    prava_strana = []

    for i in range(len(hraci_plocha)-1,-1,-1):
        if i == 0:
            continue
        horni_strana.append((0,i))

        prava_strana.append((i,len(hraci_plocha)-1))


    for x,y in horni_strana:

        symboly = []
        while x < len(hraci_plocha) and y >= 0:
            symboly.append(hraci_plocha[x][y])
            x += 1
            y -= 1
        if "XXXXX" in "".join(symboly):
            return "X"
        if "OOOOO" in "".join(symboly):
            return "O"

    for x,y in prava_strana:
        symboly = []
        while x < len(hraci_plocha) and y >= 0:

            symboly.append(hraci_plocha[x][y])
            x += 1
            y -= 1
        if "XXXXX" in "".join(symboly):
            return "X"
        if "OOOOO" in "".join(symboly):
            return "O"
    return False

hraci_pole = vytvor_pole(9)
aktualni_hrac = "O"



while True:
    vykresli_hraci_plochu(hraci_pole)
    print(f"Na řadě je hráč s {"křížky" if aktualni_hrac == "X" else "kolečky"}")
    tah_hrace(hraci_pole,aktualni_hrac)

    if kontrola_vyhry(hraci_pole):
        vykresli_hraci_plochu(hraci_pole)
        print(f"Vyhrál hráč s {"křížky"if kontrola_vyhry(hraci_pole) == "X" else "kolečky"}.")
        break

    if aktualni_hrac == "X":
        aktualni_hrac = "O"
    else:
        aktualni_hrac = "X"






