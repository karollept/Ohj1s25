#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#ympyrän pinta-ala on pi*r**2

import math

pi = math.pi
sade_str = input ("Anna ympyrän säde: ")
sade = float(sade_str)
pintaala = pi * sade ** 2
print(f"Ympyrän pinta-ala on {pintaala: .3f}")