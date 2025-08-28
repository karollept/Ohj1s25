#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

tietokone_num = str(random.randint(1, 10))
print(tietokone_num)
peli_jatkuu = True

while peli_jatkuu:
    hlo_num = str(input("Arvaa tietokoneen numero: "))
    if hlo_num == tietokone_num:
        print("Oikein, peli loppuu.")
        break
    elif hlo_num > tietokone_num:
        print("Liian suuri arvaus, arvaa uudelleen.")
    elif hlo_num < tietokone_num:
        print("Liian pieni arvaus, arvaa uudelleen.")
    else:
        print("En ymmärrä, arvaa uudelleen.")
