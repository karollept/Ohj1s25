#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

kauttaja = ("python")
salasana = ("rules")


kokeiltu = 0
mahdollisuuksia = 5

while kokeiltu < mahdollisuuksia:
    kayttaja = input("Anna käyttäjätunnus: ")
    salesana = input("Anna salasana: ")
    if kayttaja == kauttaja and salasana == salesana:
        print("Tervetuloa.")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana")
        kokeiltu = kokeiltu + 1
else:
    print("Pääsy evätty")