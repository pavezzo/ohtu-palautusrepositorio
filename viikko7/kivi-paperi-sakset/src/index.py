from luo_peli import luo_peli

def main():
    while True:
        
        print(
"""Valitse pelataanko
    (a) Ihmistä vastaan
    (b) Tekoälyä vastaan
    (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan"""
        )

        tyyppi = input()
        peli = luo_peli(tyyppi)
        
        if peli is None:
            break
        
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

        peli.pelaa()


if __name__ == "__main__":
    main()
