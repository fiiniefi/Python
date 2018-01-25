from math import ceil, sqrt
from czas import czas
from texttable import Texttable
def pierwsze_skladana(n):
    return [2] + [x for x in range(2, n) if len([d for d in range(2, ceil(sqrt(x)) + 1) if x % d == 0]) == 0]

def pierwsze_funkcyjna(n):
    return [2] + list(filter(lambda x: len(list(filter(lambda y: x % y == 0, range(2, ceil(sqrt(x)) + 1)))) == 0, range(2, n)))

def pierwsze_iterator(n):
    lista = []
    for i in KolekcjaPierwszych():
        if i < 20: lista += [i]
        else: break
    return lista

class PierwszeIterator:
    def __init__(self):
        self.licznik = 2

    def __next__(self):
        while not self.__pierwsza(self.licznik):
            self.licznik += 1
        wynik = self.licznik
        self.licznik += 1
        return wynik

    def __pierwsza(self, n):
        if n == 2: return n
        for x in range(2, ceil(sqrt(n)) + 1):
            if n % x == 0: return False
        return True

class KolekcjaPierwszych:
    def __iter__(self):
        return PierwszeIterator()

print(pierwsze_skladana(20))
print(pierwsze_funkcyjna(20))
print(pierwsze_iterator(20))
t = Texttable()
t.set_precision(6)
t.add_rows([["Wielkość danych", "Składana", "Funkcyjna", "Iterator"],
           [10, czas(pierwsze_skladana, 10), czas(pierwsze_funkcyjna, 10), czas(pierwsze_iterator, 10)],
           [100, czas(pierwsze_skladana, 100), czas(pierwsze_funkcyjna, 100), czas(pierwsze_iterator, 100)],
           [1000, czas(pierwsze_skladana, 1000), czas(pierwsze_funkcyjna, 1000), czas(pierwsze_iterator, 1000)]])
print(t.draw())
