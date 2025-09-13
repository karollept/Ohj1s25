#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='kartsu',
    password='black_rose',
    autocommit=True
    )

def lentokentät(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident =%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchall()
    return tulos

koodi = input("syötä lentoaseman ICAO-koodi: ")
kentat = lentokentät(koodi)
for kentta in kentat:
    print(f"Nimi: {kentta['name']}, ICAO: {kentta['municipality']}")

