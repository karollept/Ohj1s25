#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='kartsu',
    password='black_rose',
    autocommit=True
    )

def lentokentat(icao):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchall()

    for rivi in tulos:
        print(f"Lentokenttien koko {rivi[0]} ja määrä {rivi[1]}")
    kursori.close()

maa = input("syötä maakoodi ")
lentokentat(maa)










