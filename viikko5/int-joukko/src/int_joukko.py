KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.jono = []

    def kuuluu(self, n):
        return n in self.jono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.jono.append(n)
        return True
    
    def poista(self, n):
        if self.kuuluu(n):
            self.jono.remove(n)
            return True
        
        return False
    
    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.jono)

    def to_int_list(self):
        return self.jono

    @staticmethod
    def yhdiste(a, b):
        a = a.jono
        b = b.jono
        a.extend(b)
        r = IntJoukko()
        for x in list(set(a)):
            r.lisaa(x)
        return r
    
    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a = a.jono
        b = b.jono

        for x in a:
            if x in b:
                y.lisaa(x)
        
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a = a.jono
        b = b.jono

        for x in a:
            if x not in b:
                z.lisaa(x)
        return z
    
    def __str__(self):
        s = [str(x) for x in self.jono]
        return f"{{{', '.join(s)}}}"

