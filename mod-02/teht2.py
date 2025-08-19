"Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan."
"ympyrän pinta-ala on 2*pi*r"

import math
pi = math.pi
säde_ = input ("Anna ympyrän säde: ")
säde = float(säde_)
pintaala = 2 * pi * säde
print("Ympyrän pinta-ala on " + str(pintaala))