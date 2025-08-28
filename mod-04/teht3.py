#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
print("Kun haluat päättää ohjelman kirjoita ´---´")
numeroja = tuple()
lukuja = input("Anna minulle lukuja ")
while int(lukuja) % 1 == 0:
    numeroja = numeroja + (lukuja,)
    lukuja = input("Anna minulle lukuja ")
    if lukuja == "---":
        break

print("Isoin luku oli " + max(numeroja))
print("Ja pienin luku oli " + min(numeroja))
