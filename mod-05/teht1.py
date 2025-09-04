#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.

import random
luku = []


n = int(input("Kuinka montaa arpakuutiota käytetään "))
summa = 0

for i in range(n):
    noppa_num = random.randint(1, 6)
    summa += noppa_num
    luku.append(noppa_num)

print(luku)
print(summa)