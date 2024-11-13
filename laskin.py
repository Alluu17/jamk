
def yhteenlasku(x, y):
    return x + y

def vahennyslasku(x, y):
    return x - y

def kertolasku(x, y):
    return x * y

def jakolasku(x, y):
    if y != 0:
        return x / y
    else: 
        return "Virhe: Jakaminen nollalla ei ole mahdollista."
while True:
    print("\nValitse laskutoimitus:")
    print("1. Yhteenlasku")
    print("2. Vähennyslasku")
    print("3. Kertolasku")
    print("4. Jakolasku")
    print("5. Lopeta")  
    valinta = input("Anna valintasi (1/2/3/4/5): ")
    if valinta == '5':
        print("Laskin suljetaan. Kiitos käytöstä!")
        break
    if valinta in ('1', '2', '3', '4'):
        try:
            luku1 = float(input("Anna ensimmäinen luku: "))
            luku2 = float(input("Anna toinen luku: "))
        except ValueError:
            print("Virhe: Syötä kelvollinen numero.")
            continue
        if valinta == '1':
            print("Tulos:", yhteenlasku(luku1, luku2))

        elif valinta == '2':
            print("Tulos:", vahennyslasku(luku1, luku2))
        
        elif valinta == '3':
            print("Tulos:", kertolasku(luku1, luku2))

        elif valinta == '4':
            print("Tulos:", jakolasku(luku1, luku2))

    else:
        print("Virheellinen valinta. Yritä uudelleen.")
