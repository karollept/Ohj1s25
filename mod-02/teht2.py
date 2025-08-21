#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#ympyrän pinta-ala on pi*r**2

import math

pi = math.pi
säde_str = input ("Anna ympyrän säde: ")
säde = float(säde_str)
pintaala = pi * säde ** 2
print(f"Ympyrän pinta-ala on {pintaala: .3f}")