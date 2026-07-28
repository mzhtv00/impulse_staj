#DOSYANIZ YOKSA musteriler.csv DOSYASINI KULLANABİLİRSİNİZ

import pandas as pd
import sqlite3 as sql

con = sql.connect("musteriler.db")
print("BAĞLANDI")
curs = con.cursor()
print("CURSOR OLUŞTURULDU")

#curs.execute("DROP TABLE ABONELER")
curs.execute("""CREATE TABLE IF NOT EXISTS ABONELER(
    id INTEGER,
    ad_soyad TEXT,
    telefon INTEGER,
    eposta UNIQUE,
    adres TEXT,
    kayit_tarihi DATETIME,
    tarife TEXT,
    aylik_ucret_azn FLOAT
)""")

#dosya = input("Veri dosyanızın yolunu girin: ") #<-- kendi dosyanız varsa bu yöntemi kullanabilirsiniz

dosya = "C:/Users/Muhammed/OneDrive/Desktop/staj_projeleri/musteriler.csv"
df = pd.read_csv(dosya)
df.to_sql("GECICI_TABLO", con, if_exists = "replace", index = False)
curs.execute("""
    INSERT OR IGNORE INTO ABONELER
    SELECT * FROM GECICI_TABLO
""")
curs.execute("DROP TABLE GECICI_TABLO")
print("VERİLER EKLENDİ")

con.commit()
con.close()
