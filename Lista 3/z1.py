from math import ceil, sqrt
from czas import czas
def pierwsze_skladana(n):
    return [x for x in range(2, n) if len([d for d in range(2, ceil(sqrt(x)) + 1) if x % d == 0]) == 0]

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: len(list(filter(lambda y: x % y == 0, range(2, ceil(sqrt(x)) + 1)))) == 0, range(2, n)))

print(pierwsze_skladana(20))
print(pierwsze_funkcyjna(20))
print(czas(pierwsze_skladana, 20))
print(czas(pierwsze_funkcyjna, 20))
