#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
#Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
#Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
#Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
#Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
#Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
#(ICAO-koodi on lentoaseman yksilöivä tunniste.
#Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
#Löydät koodeja helposti selaimen avulla.)

import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='kartsu',
    password='black_rose',
    autocommit=True
    )

def lentokentät():
    sql = f"SELECT * FROM airport"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident='{koodi}'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

tehdaan = input("Mitä haluat tehdä, haluatko 1. syöttää uuden lentoaseman, 2. hakea jo syötetyn lentoaseman tiedot vai 3. lopettaa ")
while tehdaan != "3":
    if tehdaan == "1":
        koodi = input("syötä uuden lentoaseman ICAO-koodi: ")
        nimi = input("syötä uuden lentoaseman nimi: ")
        lentokentät[koodi] = nimi

    else:
        koodi2 = input("syötä lentoaseman ICAO-koodi: ")
        kentat = haeLentokentta(koodi2)
        for kentta in kentat:
            print(f"Nimi: {kentta['name']}, ICAO: {kentta['ident']}")
    tehdaan = input(
        "Mitä haluat tehdä, haluatko 1. syöttää uuden lentoaseman, 2. hakea jo syötetyn lentoaseman tiedot vai 3. lopettaa ")