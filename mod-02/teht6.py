#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random


numero1 = random.randint(1, 9)
numero2 = random.randint(1, 9)
numero3 = random.randint(1, 9)
print("Kolmenumeroinen koodi on:")
print(str(numero1)  + str(numero2) + str(numero3))

numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)
print("Nelinumeroinen koodi on:")
print(str(numero4)  + str(numero5) + str(numero6) + str(numero7))