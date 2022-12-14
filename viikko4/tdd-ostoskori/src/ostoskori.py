from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return reduce(lambda a, b: a+b.lukumaara(), self._ostokset, 0)

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return reduce(lambda a, b: a+b.hinta(), self._ostokset, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        loyty = False
        for _, x in enumerate(self._ostokset):
            if x.tuotteen_nimi() == lisattava.nimi():
                x.muuta_lukumaaraa(1)
                loyty = True
                break
        if not loyty:
            self._ostokset.append(Ostos(lisattava))
                


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for _, x in enumerate(self._ostokset):
            if x.tuotteen_nimi() == poistettava.nimi():
                x.muuta_lukumaaraa(-1)
                if x.lukumaara() == 0:
                    self._ostokset.remove(x)
                break

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
