#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

yksi_str = input("Anna ensimmäinen kokonaisluku: ")
kaksi_str = input("Anna toinen kokonaisluku: ")
kolme_str = input("Anna kolmas kokonaisluku: ")
yksi = float(yksi_str)
kaksi = float(kaksi_str)
kolme = float(kolme_str)

summa = yksi + kaksi + kolme
tulo = yksi * kaksi * kolme
keskiarvo = summa / 3
print("Kokonaislukujen summa on " + str(summa))
print("Kokonaislukujen tulo on " + str(tulo))
print("Kokonaislukujen keskiarvo on " + str(keskiarvo))
print("DONE")