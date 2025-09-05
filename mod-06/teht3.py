#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

#Yksi gallona on 3,785 litraa.


def litraa():
    gallons = int(input("Anna bensiinin määrä in gallons: "))
    while gallons >= 0:
        litra = gallons * 3.785
        print(litra)
        gallons = int(input("Anna bensiinin määrä in gallons: "))
    return

litraa()
print("Ohjelma päättyy")