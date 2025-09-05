#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa toisen listan,
#joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
#Kirjoita testausta varten pääohjelma,
#jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

kokonais = [3, 4, 6, 7, 10, 13, 16]
print(kokonais)

def karsittu():
    kokonais = [3, 4, 6, 7, 10, 13, 16]
    kokonais2 = list(filter(lambda x: x % 2 == 0, kokonais))
    print(kokonais2)
    return

karsittu()
print("Ohjelma päättyy")