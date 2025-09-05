#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

maksimisilmaluku = int(input("Anna nopan maksimisilmäluku "))
def heittaa(tahkoja):
    heitto = random.randint(1,tahkoja)
    print(heitto)
    while heitto != maksimisilmaluku:
        heitto = random.randint(1,tahkoja)
        print(heitto)
    return

heittaa(maksimisilmaluku)