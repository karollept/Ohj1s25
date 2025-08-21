#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

print("Yksi leiviskä on 20 naulaa.")
print("Yksi naula on 32 luotia.")
print("Yksi luoti on 13,3 grammaa.")
print("Kerro massa keskiaikaisten mittojen mukaan")
leiviskat = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")
leiviskat = float(leiviskat)
naulat = float(naulat)
luodit = float(luodit)

#kaikkien asioiden paino grammoissa
luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

paino_yht = luoti * luodit + naula * naulat + leiviska * leiviskat
kilo = paino_yht // 1000
gramma = paino_yht % 1000

print("Massa nykymittojen mukaan:")
print(str(kilo) + " kilogrammoissa ja " + str(gramma) + " grammaa.")
