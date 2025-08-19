#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
#Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = input("Anna suorakulmion kannan pituus: ")
kanta = float(kanta)
korkeus = input("Anna suorakulmion korkeus: ")
korkeus = float(korkeus)

piiri = kanta + kanta + korkeus + korkeus
print("Suorakulmion piiri on " + str(piiri))
pintaala = kanta * korkeus
print("Suorakulmion pinta-ala on " + str(pintaala))