class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class Summa:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote
        self._edellinen = 0

    def suorita(self):
        self._edellinen = self._sovellus.tulos
        self._sovellus.plus(int(self._syote()))

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)

class Erotus:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote
        self._edellinen = 0

    def suorita(self):
        self._edellinen = self._sovellus.tulos
        self._sovellus.miinus(int(self._syote()))
    
    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)


class Nollaus:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote
        self._edellinen = 0

    def suorita(self):
        self._edellinen = self._sovellus.tulos
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)


class Kumoa:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote
        self.edellinen_komento = None

    def suorita(self):
        self.edellinen_komento.kumoa()


