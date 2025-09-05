#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

def heittaa():
    heitto = random.randint(1,6)
    print(heitto)
    while heitto != 6:
        heitto = random.randint(1,6)
        print(heitto)
    return
heittaa()