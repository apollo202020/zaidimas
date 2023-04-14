skaiciu_laukas = ["7 | 8 | 9", "4 | 5 | 6", "1 | 2 | 3"]
for laukas in skaiciu_laukas:
    print(laukas)

zaideju_ejimai = 0
zaidejas = "X"
zaidejas1 = "O"


while True:
    if zaidejas == "X":
        x = input("Zaidejas X iveskite veiksma: ")
        if x.isdigit() and int(x) in range(1, 10):
            x = int(x)
            if x == 7:
                pirmi = skaiciu_laukas[0].split()
                if pirmi[0] == "X" or pirmi[0] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[0] = "X"
                skaiciu_laukas[0] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 8:
                pirmi = skaiciu_laukas[0].split()
                if pirmi[2] == "X" or pirmi[2] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[2] = "X"
                skaiciu_laukas[0] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 9:
                pirmi = skaiciu_laukas[0].split()
                if pirmi[4] == "X" or pirmi[4] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[4] = "X"
                skaiciu_laukas[0] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 4:
                pirmi = skaiciu_laukas[1].split()
                if pirmi[0] == "X" or pirmi[0] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[0] = "X"
                skaiciu_laukas[1] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 5:
                pirmi = skaiciu_laukas[1].split()
                if pirmi[2] == "X" or pirmi[2] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[2] = "X"
                skaiciu_laukas[1] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 6:
                pirmi = skaiciu_laukas[1].split()
                if pirmi[4] == "X" or pirmi[4] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[4] = "X"
                skaiciu_laukas[1] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 1:
                pirmi = skaiciu_laukas[2].split()
                if pirmi[0] == "X" or pirmi[0] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[0] = "X"
                skaiciu_laukas[2] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 2:
                pirmi = skaiciu_laukas[2].split()
                if pirmi[2] == "X" or pirmi[2] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[2] = "X"
                skaiciu_laukas[2] = " ".join(pirmi)
                zaideju_ejimai += 1
            elif x == 3:
                pirmi = skaiciu_laukas[2].split()
                if pirmi[4] == "X" or pirmi[4] == "O":
                    print("Laukelis uzimtas")
                    continue
                pirmi[4] = "X"
                skaiciu_laukas[2] = " ".join(pirmi)
                zaideju_ejimai += 1

        if x not in range(1, 10):
            print("Zaidejo X klaida, iveskite skaiciu nuo 1 iki 9")
            continue


        for laukas in skaiciu_laukas:
            print(laukas)

    # LAIMEJIMO NUSTATYMAS
    if x not in skaiciu_laukas:
        pirmi = skaiciu_laukas[2].split()
        antri = skaiciu_laukas[1].split()
        treti = skaiciu_laukas[0].split()
        # EILUCIU LAIMEJIMAS
        if pirmi[4] == "X" and pirmi[2] == "X" and pirmi[0] == "X":
            print("Zaidejas X laimejo pirma eilute!")
            break
        elif antri[4] == "X" and antri[2] == "X" and antri [0] == "X":
            print("Zaidejas X laimejo antra eilute!")
            break
        elif treti[4] == "X" and treti[2] == "X" and treti[0] == "X":
            print("Zaidejas X laimejo trecia eilute!")
            break
        # STULPELIU LAIMEJIMAS
        elif treti[4] == "X" and antri[4] == "X" and pirmi[4] == "X":
            print("Zaidejas X laimejo treciu stulpeliu!")
            break
        elif treti[2] == "X" and antri[2] == "X" and pirmi[2] == "X":
            print("Zaidejas X laimejo antru stulpeliu!")
            break
        elif treti[0] == "X" and antri[0] == "X" and pirmi[0] == "X":
            print("Zaidejas X laimejo pirmi sulpeliu!")
            break
        # ISTRIZAINES LAIMEJIMAS
        elif treti[0] == "X" and antri[2] == "X" and pirmi[4] == "X":
            print("Zaidejas X  laimejo istrizaine is kaires!")
            break
        elif treti[4] == "X" and antri[2] == "X" and pirmi[0] == "X":
            print("Zaidejas X  laimejo istrizaine is desines!")
            break

    # JEIGU LYGIOSIOS
    if zaideju_ejimai == 9:
        print("Zaidimas baigesi lygiosiomis!")
        break
    while True:

        if zaidejas1 == "O":
            o = input("Zaidejas O iveskite veiksma: ")
            if o.isdigit() and int(o) in range(1, 10):
                o = int(o)
                if o == 7:
                    pirmi = skaiciu_laukas[0].split()
                    if pirmi[0] == "X":
                        print("Laukelis uzimtas")
                        continue
                    elif pirmi[0] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[0] = "O"
                    skaiciu_laukas[0] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 8:
                    pirmi = skaiciu_laukas[0].split()
                    if pirmi[2] == "X":
                        print("Laukelis uzimtas")
                        continue
                    elif pirmi[2] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[2] = "O"
                    skaiciu_laukas[0] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 9:
                    pirmi = skaiciu_laukas[0].split()
                    if pirmi[4] == "X":
                        print("Laukelis uzimtas")
                        continue
                    elif pirmi[4] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[4] = "O"
                    skaiciu_laukas[0] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 4:
                    pirmi = skaiciu_laukas[1].split()
                    if pirmi[0] == "X":
                        print("Laukelis uzimtas")
                        continue
                    elif pirmi[0] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[0] = "O"
                    skaiciu_laukas[1] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 5:
                    pirmi = skaiciu_laukas[1].split()
                    if pirmi[2] == "X":
                        print("Laukelis uzimtas")
                        continue
                    elif pirmi[2] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[2] = "O"
                    skaiciu_laukas[1] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 6:
                    pirmi = skaiciu_laukas[1].split()
                    if pirmi[4] == "X":
                        print("Laukelis uzimtas X zaidejo")
                        continue
                    elif pirmi[4] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[4] = "O"
                    skaiciu_laukas[1] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 1:
                    pirmi = skaiciu_laukas[2].split()
                    if pirmi[0] == "X":
                        print("Laukelis uzimtas X zaidejo")
                        continue
                    elif pirmi[0] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[0] = "O"
                    skaiciu_laukas[2] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 2:
                    pirmi = skaiciu_laukas[2].split()
                    if pirmi[2] == "X":
                        print("Laukelis uzimtas X zaidejo")
                        continue
                    elif pirmi[2] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[2] = "O"
                    skaiciu_laukas[2] = " ".join(pirmi)
                    zaideju_ejimai += 1
                elif o == 3:
                    pirmi = skaiciu_laukas[2].split()
                    if pirmi[4] == "X":
                        print("Laukelis uzimtas X zaidejo")
                        continue
                    elif pirmi[4] == "O":
                        print("Laukelis uzimtas O zaidejo")
                        continue
                    pirmi[4] = "O"
                    skaiciu_laukas[2] = " ".join(pirmi)
                    zaideju_ejimai += 1
                for laukas in skaiciu_laukas:
                    print(laukas)
                if o in range(1, 10):
                    break

        if o not in range(1, 10):
            print("Zaidejo O klaida, iveskite skaiciu nuo 1 iki 9")
            continue

        for laukas in skaiciu_laukas:
            print(laukas)

    # LAIMEJIMO NUSTATYMAS
    if o not in skaiciu_laukas:
        pirmi = skaiciu_laukas[2].split()
        antri = skaiciu_laukas[1].split()
        treti = skaiciu_laukas[0].split()
        # EILUCIU LAIMEJIMAS
        if pirmi[4] == "O" and pirmi[2] == "O" and pirmi[0] == "O":
            print("Zaidejas O laimejo pirma eilute!")
            break
        elif antri[4] == "O" and antri[2] == "O" and antri[0] == "O":
            print("Zaidejas O laimejo antra eilute!")
            break
        elif treti[4] == "O" and treti[2] == "O" and treti[0] == "O":
            print("Zaidejas O laimejo trecia eilute!")
            break
        # STULPELIU LAIMEJIMAS
        elif treti[4] == "O" and antri[4] == "O" and pirmi[4] == "O":
            print("Zaidejas O laimejo treciu stulpeliu!")
            break
        elif treti[2] == "O" and antri[2] == "O" and pirmi[2] == "O":
            print("Zaidejas O laimejo antru stulpeliu!")
            break
        elif treti[0] == "O" and antri[0] == "O" and pirmi[0] == "O":
            print("Zaidejas O laimejo pirmi sulpeliu!")
            break
        # ISTRIZAINES LAIMEJIMAS
        elif treti[0] == "O" and antri[2] == "O" and pirmi[4] == "O":
            print("Zaidejas O  laimejo istrizaine is kaires!")
            break
        elif treti[4] == "O" and antri[2] == "O" and pirmi[0] == "O":
            print("Zaidejas O  laimejo istrizaine is desines!")
            break
