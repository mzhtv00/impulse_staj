from db_class import MySqlDB

db = MySqlDB()
db.connect()

db.db_olustur("impulsedb")
db.tablo_olustur("impulsedb", "kullanicilar", 
                 """id INT AUTO_INCREMENT PRIMARY KEY,
                    ad_soyad VARCHAR(50) NOT NULL,
                    mail VARCHAR(200) UNIQUE NOT NULL,
                    telefon VARCHAR(20) NOT NULL,
                    adres TEXT NOT NULL,
                    tarife VARCHAR(20),
                    kayıt_tarihi DATETIME
                """)
db.tablo_olustur("impulsedb", "tarifeler", 
                 """id INT AUTO_INCREMENT PRIMARY KEY,
                 tarife VARCHAR(20) NOT NULL,
                 hız_mbps INT,
                 ücret_azn INT
                 """)

tarifeler = [
    ("Standart", 50, 25),
    ("Premium", 200, 50),
    ("Business", 500, 90),
    ("Ultra", 1000, 150)
]
#db.tarife_ekle(tarifeler)

kullanici = [
    ("Abone1", "abone100@gmail.com", "+90 555 444 33 22", "Kocaeli, İzmit", "Standart"),
    ("Abone2", "abone200@gmail.com", "+90 555 222 33 44", "Bursa, Nilüfer", "Premium")
]
db.kullanici_ekle(kullanici)


db.disconnect()