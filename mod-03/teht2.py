#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen
#kuvauksen alla olevan luettelon mukaisesti.
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hytti = input("Kerro hyttiluokkasi hyttisi kuvausta varten: ")

if (hytti == "LUX" or hytti == "lux" or hytti == "Lux"):
    print("Hyttisi LUX on parvekkeellinen hytti yläkannella.")

elif (hytti == "A" or hytti == "a"):
    print("Hyttisi A on ikkunallinen hytti autokannen yläpuolella.")

elif (hytti == "B" or hytti == "b"):
    print("Hyttisi B on ikkunaton hytti autokannen yläpuolella.")

elif (hytti == "C" or hytti == "c"):
    print("Hyttisi C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")