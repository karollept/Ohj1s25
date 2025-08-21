#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
#montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = input("Kuinka pitkä on kuha? ")
kuha = float(kuha)
alipaino = 37-kuha
alipaino = str(alipaino)
if kuha < 37:
    print("Laske kuha takaisin järveen kuha on " + alipaino + " senttiä alle sallitusta pyyntimitasta.")