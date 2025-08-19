#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

yksi = input("Anna ensimmäinen kokonaisluku: ")
kaksi = input("Anna toinen kokonaisluku: ")
kolme = input("Anna kolmas kokonaisluku: ")
yksi = float(yksi)
kaksi = float(kaksi)
kolme = float(kolme)

summa = yksi + kaksi + kolme
tulo = yksi * kaksi * kolme
keskiarvo = summa / 3
print("Kokonaislukujen summa on " + str(summa))
print("Kokonaislukujen tulo on " + str(tulo))
print("Kokonaislukujen keskiarvo on " + str(keskiarvo))
print("DONE")