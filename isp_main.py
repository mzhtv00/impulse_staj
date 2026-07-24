from db_class import MySqlDB

db = MySqlDB()
db.connect()

while True:
    print("\n1. Kullanıcı Ekle\n2. Çıkış\n")
    choice = int(input("İşlem seçin: "))
    if (choice == 1):
        ad_soyad = input("Ad Soyad: ").strip()
        mail = input("Mail: ").strip()
        telefon = input("Telefon: ").strip()
        adres = input("Adres: ")
        if not telefon.isdigit():
            print("Lütfen geçerli bir numara girin.")
            continue
        kullanici_verileri = {"ad_soyad": ad_soyad, "mail": mail, "telefon": telefon, "adres": adres}
        db.insert_record("kullanicilar", kullanici_verileri)

    elif (choice == 2):
        print("Çıkış yapılıyor..")
        break

    else:
        print("Geçersiz giriş.")

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

#tarifeler = [
#    ("Standart", 50, 25),
#    ("Premium", 200, 50),
#    ("Business", 500, 90),
#    ("Ultra", 1000, 150)
#]

db.disconnect()
