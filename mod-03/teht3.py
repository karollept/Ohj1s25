#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

biolog_s = input("Kerro biologinen sukupuolesi: ")
hemogl_a = float(input("Kerro sinun hemoglobiiniarvo: "))

if (biolog_s == "Nainen" or biolog_s == "NAINEN" or biolog_s == "nainen"):
    if (hemogl_a >= 117 and hemogl_a <= 175):
        print("Hemoglobiiniarvosi on normaali.")
    elif hemogl_a > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on alhainen.")

elif (biolog_s == "Mies" or biolog_s == "MIES" or biolog_s == "mies"):
    if (hemogl_a >= 134 and hemogl_a <= 195):
        print("Hemoglobiiniarvosi on normaali.")
    elif hemogl_a > 185:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on alhainen.")

else:
    print("En ymmärtänyt.")
