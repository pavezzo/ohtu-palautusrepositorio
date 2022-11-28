from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return len(self.ostokset)

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return reduce(lambda a, b: a+b.hinta(), self.ostokset, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        loyty = False
        for i, x in enumerate(self.ostokset):
            if x.tuotteet_niim() == lisattava.nimi():
                x.muuta_lukumaaraa(1)
                loyty = True
                break
        if not loyty:
            self.ostokset.append(Ostos(lisattava))
                


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
