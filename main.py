from modellek.belfoldi_jarat import BelfoldiJarat
from modellek.nemzetkozi_jarat import NemzetkoziJarat
from modellek.legitarsasag import LegiTarsasag
from modellek.jegy_foglalas import JegyFoglalas

def feltoltott_adatok():
    legitarsasag = LegiTarsasag("Pinter AirHungary")

    j1 = BelfoldiJarat("B101", "Budapest", 54000)
    j2 = NemzetkoziJarat("K420", "Kingston", 240000)
    j3 = NemzetkoziJarat("R303", "Rome", 140000)

    legitarsasag.jarat_hozzaadas(j1)
    legitarsasag.jarat_hozzaadas(j2)
    legitarsasag.jarat_hozzaadas(j3)

    foglalasok = [
        JegyFoglalas("Dwayne Johnson", j1),
        JegyFoglalas("Minta Béla", j2),
        JegyFoglalas("Barck Obama", j3),
        JegyFoglalas("Bill Clinton", j1),
        JegyFoglalas("Pintér Olivér", j3),
        JegyFoglalas("Nikola Tesla", j2),
    ]

    return legitarsasag, foglalasok

def jegy_foglalas(foglalasok, legitarsasag):
    nev = input("Kérjük adja meg a nevét: ")
    jaratszam = input("Kérjük adja meg a foglalni kívánt járatszámot: ")
    jarat = legitarsasag.jarat_kereses(jaratszam)
    if jarat:
        foglalas = JegyFoglalas(nev, jarat)
        foglalasok.append(foglalas)
        print(f"A tranzackió sikeresen végbe ment! Ön által fizetendő összeg: {jarat.jegyar} Ft")
    else:
        print("Hibás járatszám")

def foglalas_lemondas(foglalasok):
    nev = input("Kérjük adja meg a nevét: ")
    jaratszam = input("Kérjük adja meg a járatszámot: ")
    for f in foglalasok:
        if f.utas_nev == nev and f.jarat.jaratszam == jaratszam:
            foglalasok.remove(f)
            print("Foglalása sikeresen törölve. Reméljük, hogy hamarosan újra utazik velünk!")
            return
    print("Nem található ilyen foglalás.")

def jaratok_listazasa(legitarsasag):
    jaratok = legitarsasag.jaratok
    if not jaratok:
        print("Nincsenek elérhető járatok.")
    else:
        print("Elérhető járatok:")
        for jarat in jaratok:
            print(f"{jarat.jaratszam} - {jarat.celallomas} ({jarat.get_jarat_tipus()}) - {jarat.jegyar} Ft")

def foglalasok_listazasa(foglalasok):
    if not foglalasok:
        print("Nincsenek aktív foglalások.")
    else:
        for f in foglalasok:
            print(f"{f.utas_nev} - {f.jarat.jaratszam} ({f.jarat.celallomas}) [{f.jarat.get_jarat_tipus()}]")

def main():
    legitarsasag, foglalasok = feltoltott_adatok()

    while True:
        print("\n=== AIR Pinter Foglalási Rendszer ===")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy műveletet: ")
        match valasztas:
            case "1":
                jegy_foglalas(foglalasok, legitarsasag)
            case "2":
                foglalas_lemondas(foglalasok)
            case "3":
                foglalasok_listazasa(foglalasok)
            case "4":
                jaratok_listazasa(legitarsasag)
            case "5":
                print("Kilépés...Reméljük, hogy hamarosan újra utazik velünk!")
                break
            case _:
                print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
