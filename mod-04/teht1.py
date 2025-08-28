#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
luku = 1000
print("luvut jokta ovat jaollisia luvulla kolme väliltä 1-1000 ovat")
while  luku >= 3:
    if luku % 3 == 0:
        print(luku)
        luku = luku - 1
    else:
        luku = luku - 1

