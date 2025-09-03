#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.

import random
luku = []


n = int(input("Kuinka montaa arpakuutiota käytetään "))
summa = 0
kertaa = 0

for i in range(n):
    noppa_num = random.randint(1, 6)
    summa += noppa_num
    luku.append(noppa_num)
    kertaa = kertaa + 1

print(luku)
print(summa)