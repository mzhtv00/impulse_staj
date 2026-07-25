from db_class import MySqlDB

db = MySqlDB()
db.connect()
database = db.db_olustur("impulsedb")
db.disconnect()
db.connect(database = database)
db.tablo_olustur(database, "kullanicilar", 
                 """id INT AUTO_INCREMENT PRIMARY KEY,
                    ad_soyad VARCHAR(50) NOT NULL,
                    mail VARCHAR(200) UNIQUE NOT NULL,
                    telefon VARCHAR(20) NOT NULL,
                    adres TEXT NOT NULL,
                    tarife VARCHAR(20),
                    kayıt_tarihi DATETIME""")

db.tablo_olustur(database, "tarifeler", 
             """id INT AUTO_INCREMENT PRIMARY KEY,
                tarife VARCHAR(20) UNIQUE,
                hız_mbps INT,
                ücret_azn INT""")

tarifeler = [
    {"tarife": "Standart", "hız_mbps": 50,  "ücret_azn": 25},
    {"tarife": "Premium",  "hız_mbps": 200, "ücret_azn": 50},
    {"tarife": "Business", "hız_mbps": 500, "ücret_azn": 90},
    {"tarife": "Ultra",    "hız_mbps": 1000,"ücret_azn": 150}
]
for t in tarifeler:
    db.insert_ignore("tarifeler", t)

tarife_adi = [t["tarife"] for t in tarifeler]

while True:
    print("\n1. Kullanıcı Ekle\n2. Veri Görüntüle\n3. Çıkış\n")
    choice = int(input("İşlem seçin: "))
    if (choice == 1):
        ad_soyad = input("Ad Soyad: ").strip()
        mail = input("Mail: ").strip()
        telefon = input("Telefon: ").strip()
        adres = input("Adres: ")

        if not telefon.isdigit():
            print("Lütfen geçerli bir numara girin.")
            continue

        print(f"Mevcut tarifeler: {tarife_adi}")
        tarife = input("Tarife seçin: ").strip()
        if tarife not in tarife_adi:
            print("Geçersiz tarife.")
            continue

        musteri_verileri = {
            "ad_soyad": ad_soyad, 
            "mail": mail, 
            "telefon": telefon, 
            "adres": adres, 
            "tarife": tarife, 
            "kayıt_tarihi": None
            }
        db.insert_record("kullanicilar", musteri_verileri)
        print(f"{ad_soyad} başarıyla eklendi.")

    elif choice == 2:
        print("\n1. Tüm satırlar\n2. Tek satır\n")
        secim = int(input("Görüntülemek istediğinizi seçin: "))

        if secim == 1:
            sonuc = db.get_rows("SELECT * FROM kullanicilar")
            if not sonuc:
                print("Görüntülenecek veri yok.")
            else:
                for item in sonuc:
                    print(item)
        elif secim == 2:
            rows = db.get_rows("SELECT * FROM kullanicilar")
            if not rows:
                print("Görüntülenebilecek satır yok.")
                continue
            try:
                satir = int(input("Satır numarası: "))
            except ValueError:
                print("Geçersiz giriş.")
                continue

            if 1 <= satir <= len(rows):
                print(rows[satir - 1])
            else:
                print(f"Geçersiz sayı. 1 ile {len(rows)} arası sayı girin.")

    elif (choice == 3):
        print("Çıkış yapılıyor..")
        break

    else:
        print("Geçersiz giriş.")

db.disconnect()
