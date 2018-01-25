import abc
import itertools

class Formula:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError("Klasa Formula jest wirtualna!")

    @abc.abstractmethod
    def oblicz(self, zmienne):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def pobierzZmienne(self):
        pass



class Zmienna(Formula):
    def __init__(self, nazwa):
        self.nazwa = str(nazwa)

    def oblicz(self, zmienne):
        return zmienne[self.nazwa]

    def __str__(self):
        return (self.nazwa)

    def pobierzZmienne(self):
        return [self.nazwa]



class Stala(Formula):
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def oblicz(self, zmienne):
        return self.wartosc

    def __str__(self):
        return (str(self.wartosc))

    def pobierzZmienne(self):
        return []



class Negacja(Formula):
    def __init__(self, wyrazenie):
        self.wyrazenie = wyrazenie

    def oblicz(self, zmienne):
        return not (self.wyrazenie.oblicz(zmienne))

    def __str__(self):
        return (chr(172) + "(" + str(self.wyrazenie) + ")")

    def pobierzZmienne(self):
        return self.wyrazenie.pobierzZmienne()



class Binarny(Formula):
    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    @abc.abstractmethod
    def oblicz(self, zmienne):
        pass

    @abc.abstractmethod
    def __str__(self, zmienne):
        pass

    def pobierzZmienne(self):
        return self.lewy.pobierzZmienne() + self.prawy.pobierzZmienne()



class Koniunkcja(Binarny):
    def __init__(self, lewy, prawy):
        Binarny.__init__(self, lewy, prawy)

    def oblicz(self, zmienne):
        return self.lewy.oblicz(zmienne) and self.prawy.oblicz(zmienne)

    def __str__(self):
        return ("(" + str(self.lewy) + " ^ " + str(self.prawy) + ")")



class Alternatywa(Binarny):
    def __init__(self, lewy, prawy):
        Binarny.__init__(self, lewy, prawy)

    def oblicz(self, zmienne):
        return self.lewy.oblicz(zmienne) or self.prawy.oblicz(zmienne)

    def __str__(self):
        return ("(" + str(self.lewy) + " v " + str(self.prawy) + ")")



class Implikacja(Binarny):
    def __init__(self, lewy, prawy):
        Binarny.__init__(self, lewy, prawy)

    def oblicz(self, zmienne):
        return not (self.lewy.oblicz(zmienne) and not self.prawy.oblicz(zmienne))

    def __str__(self):
        return ("(" + str(self.lewy) + " => " + str(self.prawy) + ")")



class Rownowaznosc(Binarny):
    def __init__(self, lewy, prawy):
        Binarny.__init__(self, lewy, prawy)

    def oblicz(self, zmienne):
        return self.lewy.oblicz(zmienne) == self.prawy.oblicz(zmienne)

    def __str__(self):
        return ("(" + str(self.lewy) + " <=> " + str(self.prawy) + ")")



def czyTautologia(formula):
    zmienne = list(set(formula.pobierzZmienne()))
    produkt = itertools.product([False, True], repeat = len(zmienne))
    slownik = ({k: v for k, v in zip(zmienne, prod)} for prod in produkt)
    for i in slownik:
        if not formula.oblicz(i):
            return False
    return True



def main():
    formula = Alternatywa(Zmienna("x"), Negacja(Zmienna("x")))
    print("Czy ", formula, " jest tautologia? ", czyTautologia(formula), sep = "", end = "\n")
    formula2 = Implikacja(Rownowaznosc(Zmienna("x"), Stala(True)), Koniunkcja(Zmienna("y"), Zmienna("x")))
    print("Czy ", formula2, " jest tautologia? ", czyTautologia(formula2), sep = "", end = "\n")
    print("Czy spelnione? ", formula.oblicz({"x":True}))
    print("Czy spelnione? ", formula2.oblicz({"x":False, "y":True}))


main()
