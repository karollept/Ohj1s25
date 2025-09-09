#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

kuukaus = int(input("Anna kuukauden numero "))
vuoden_ajat = {1:"Talvella",
               2:"Talvella",
               3:"Keväällä",
               4:"Keväällä",
               5:"Keväällä",
               6:"Kesällä",
               7:"Kesällä",
               8:"Kesällä",
               9:"Syksyllä",
               10:"Syksyllä",
               11:"Syksyllä",
               12:"Talvella"}

vuo_aika = vuoden_ajat[kuukaus]

print (f"{kuukaus}. on {vuo_aika}.")

