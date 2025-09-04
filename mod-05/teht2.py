#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numeroja = []
lukuja = str(input("Anna minulle lukuja "))
while lukuja != "":
    numeroja = numeroja + [lukuja,]
    lukuja = str(input("Anna minulle lukuja "))

numeroja.sort(reverse=True)
print("Isoimmat viisi lukua oli ")
print(numeroja[0:5])