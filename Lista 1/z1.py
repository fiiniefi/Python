import random
import sys

def glowna_gra(n):
    i=0
    count = [0,0]
    while i < n or count[0] == count[1]:
        p1 = rzut_kostka() + rzut_kostka()
        p2 = rzut_kostka() + rzut_kostka()
        if p1 == p2:
            count[0], count[1] = count[0] + 1, count[1] + 1
        else:
            count[int(p2 > p1)] += 1
        print("Wynik tury:\nGracz pierwszy: ", p1, "\nGracz drugi: ", p2, sep = "")
        print("Wynik ogólny po turze numer ", i+1, ": ", count[0], " - ", count[1], sep = "", end = "\n\n")
        i += 1
    print("\n\nWYNIK KOŃCOWY: ", count[0], " - ", count[1], sep = "")



def rzut_kostka():
    return random.randint(1, 6)

glowna_gra(int(sys.argv[1]))
