from functools import reduce
class StrumienIterator:
    def __init__(self, sciezka):
        self.plik = open(sciezka, "r")

    def __next__(self):
        if self.plik.closed:
            raise StopIteration
        s = ""
        akapit = ""
        while s != '\t':
            akapit += s
            s = self.plik.read(1)
            if not s:
                self.plik.close()
                break
        return akapit

    def __iter__(self):
        return self

"""def przetworz_plik(plik):
    with open(plik, 'r') as f:
        current_par = ""
        for line in f:
            if "\t" in line and current_par:
                yield current_par
            else:
                current_par += line"""

def formatuj_akapit(akapit, szerokosc):
    podzielone = akapit.split('\n')
    podzielone = list(map(lambda x: (x[:szerokosc+1]), podzielone))
    return reduce(lambda x, y: x + '\n' + y, podzielone)



lista = []
for i in StrumienIterator("z1 with paragraphs.py"):
    lista += [i]
lista = list(map(lambda x: formatuj_akapit(x, 30), lista))
print(reduce(lambda x, y: x + y, lista))
