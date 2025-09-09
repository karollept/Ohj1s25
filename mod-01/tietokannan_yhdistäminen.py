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

code = input("syötä koodi: ")
kentat = haeLentokentta(code)

for kentta in kentat:
    print(f"Nimi: {kentta['name']}, ICAO: {kentta['ident']}")