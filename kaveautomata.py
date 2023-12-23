"""
A program egy kávéautomata működését szimulálja
"""

# italválasztó menü

ital = input("Üdvözöljük! A következő lehetőségek közül válasszon italt a zárójelben megadott betűkkel! Minden ital 200 Ft + kiegészítőnként 20 Ft: KÁVÉ(K), TEA(T), FORRÓCSOKI(F): ")

italok = ["K","k","T","t","F","f"]

while ital not in italok:
    print("Kérem a megadott betűkkel válaszoljon")
    ital = input("Üdvözöljük! A következő lehetőségek közül válasszon italt a zárójelben megadott betűkkel!: KÁVÉ(K), TEA(T), FORRÓCSOKI(F): ")

osszeg = 0

# kávé kiegészítő menü

if ital == "K" or ital == "k":
    osszeg += 200
    print(f"Az összeg jelenleg: {osszeg}")
    valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    opciok = ["igen", "nem", "Igen", "Nem", "IGEN", "NEM"]
    while valasz not in opciok:
        print("Kérem a megadott opciókból válasszon!")
        valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    if valasz == "nem":
        print(f"A végleges összeg: {osszeg}") 
    elif valasz == "igen":
        tej = input("Kér bele tejet? (igen/nem): ")
        while tej not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            tej = input("Kér bele tejet? (igen/nem): ")
        if tej == "nem":
            print(f"Az összeg jelenleg: {osszeg}") 
        elif tej == "igen":
            osszeg += 20
            print(f"Az összeg jelenleg: {osszeg}")
        tejszin = input("Kér bele tejszínt? (igen/nem): ")
        while tejszin not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            tejszin = input("Kér bele tejszínt? (igen/nem): ")
        if tejszin == "nem":
            print(f"Az összeg jelenleg: {osszeg}")
        elif tejszin == "igen": 
            osszeg += 20 
            print(f"Az összeg jelenleg: {osszeg}")
        cukor = input("Kér bele cukrot? (igen/nem): ")
        while cukor not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            cukor = input("Kér bele cukrot? (igen/nem): ")
        if cukor == "nem":
            print(f"A végleges összeg: {osszeg}") 
        elif cukor == "igen":
            osszeg += 20 
            print(f"A végleges összeg: {osszeg}")

# tea kiegészítő menü
            
if ital == "T" or ital == "t":
    osszeg += 200
    print(f"Az összeg jelenleg: {osszeg}")
    valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    opciok = ["igen", "nem", "Igen", "Nem", "IGEN", "NEM"]
    while valasz not in opciok:
        print("Kérem a megadott opciókból válasszon!")
        valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    if valasz == "nem":
        print(f"A végleges összeg: {osszeg}") 
    elif valasz == "igen":
        tej = input("Kér bele tejet? (igen/nem): ")
        while tej not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            tej = input("Kér bele tejet? (igen/nem): ")
        if tej == "nem":
            print(f"Az összeg jelenleg: {osszeg}") 
        elif tej == "igen":
            osszeg += 20
            print(f"Az összeg jelenleg: {osszeg}")
        citrom = input("Kér bele citromot? (igen/nem): ")
        while citrom not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            citrom = input("Kér bele citromot? (igen/nem): ")
        if citrom == "nem":
            print(f"Az összeg jelenleg: {osszeg}")
        elif citrom == "igen": 
            osszeg += 20 
            print(f"Az összeg jelenleg: {osszeg}")
        cukor = input("Kér bele cukrot? (igen/nem): ")
        while cukor not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            cukor = input("Kér bele cukrot? (igen/nem): ")
        if cukor == "nem":
            print(f"A végleges összeg: {osszeg}") 
        elif cukor == "igen":
            osszeg += 20 
            print(f"A végleges összeg: {osszeg}")

# forrócsoki kiegészítő menü

if ital == "F" or ital == "f":
    osszeg += 200
    print(f"Az összeg jelenleg: {osszeg}")
    valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    opciok = ["igen", "nem", "Igen", "Nem", "IGEN", "NEM"]
    while valasz not in opciok:
        print("Kérem a megadott opciókból válasszon!")
        valasz = input("Kér hozzá bármilyen kiegészítőt? (igen/nem): ")
    if valasz == "nem":
        print(f"A végleges összeg: {osszeg}") 
    elif valasz == "igen":
        tej = input("Kér bele tejet? (igen/nem): ")
        while tej not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            tej = input("Kér bele tejet? (igen/nem): ")
        if tej == "nem":
            print(f"Az összeg jelenleg: {osszeg}") 
        elif tej == "igen":
            osszeg += 20
            print(f"Az összeg jelenleg: {osszeg}")
        tejszin = input("Kér bele tejszínt? (igen/nem): ")
        while tejszin not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            tejszin = input("Kér bele tejszínt? (igen/nem): ")
        if tejszin == "nem":
            print(f"Az összeg jelenleg: {osszeg}")
        elif tejszin == "igen": 
            osszeg += 20 
            print(f"Az összeg jelenleg: {osszeg}")
        cukor = input("Kér bele cukrot? (igen/nem): ")
        while cukor not in opciok:
            print("Kérem a megadott opciókból válasszon!")
            cukor = input("Kér bele cukrot? (igen/nem): ")
        if cukor == "nem":
            print(f"A végleges összeg: {osszeg}") 
        elif cukor == "igen":
            osszeg += 20 
            print(f"A végleges összeg: {osszeg}")