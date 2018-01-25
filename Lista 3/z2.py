from math import floor
from czas import czas
def doskonale_skladana(n):
    return [x for x in range(2, n) if sum([d for d in range(1, floor(x/2) + 1) if x % d == 0]) == x]

def doskonale_funkcyjna(n):
    return list(filter(lambda x: sum(list(filter(lambda y: x % y == 0, range(1, floor(x/2) + 1)))) == x, range(2, n)))

print(doskonale_skladana(10000))
print(doskonale_funkcyjna(10000))
print(czas(doskonale_skladana, 10000))
print(czas(doskonale_funkcyjna, 10000))
