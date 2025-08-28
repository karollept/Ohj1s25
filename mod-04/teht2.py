#Ohjelma tuumat to cm till input is negative
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

#1 tuuma = 2.54 cm
tuuma = float(input("Anna tuuma "))
while tuuma >= 0:
    sent = tuuma * 2.54
    print("Antamasi tuumat muutettuna sentimetreihin on " + str(sent) + "cm")
    tuuma = float(input("Anna tuuma "))
print("Lopetan toiminnan")
