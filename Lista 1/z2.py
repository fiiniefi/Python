def xor(x, y):
    return ( (x | y) & (~x | ~y) )

def zaszyfruj(word, key):
    result = ""
    for i in range (len(word)):
        result += chr(xor(ord(word[i]), key))
    return result

odszyfruj = zaszyfruj


key = 7
encrypted = zaszyfruj("Python", key)
print(encrypted)
print(odszyfruj(encrypted, key))
