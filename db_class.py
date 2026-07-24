import mysql.connector


class MySqlDB:
    def __init__(self): # <-- database eklenebilir
        self.__host =  "localhost"
        self.__user = "root"
        self.__password = "root"
        #self.__database = "impulsedb"  eğer mevcut database'niz varsa 9 ve 18ci satırları kullanabilirsiniz.
        self.__connect = None
        self.__cursor = None

    def connect(self):
        self.__connect = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            #database = self.__database
        )
        if self.__connect.is_connected():
            self.__cursor = self.__connect.cursor()
            print("Bağlantı başarılı.")
        else:
            print("Bağlantı başarısız.")

    def db_olustur(self, db_adi, charset = "utf8mb4", collation = "utf8mb4_0900_ai_ci"):
        sql = f"CREATE DATABASE IF NOT EXISTS {db_adi} CHARACTER SET {charset} COLLATE {collation}"
        self.__cursor.execute(sql)
        print(f"'{db_adi}' database'i oluşturuldu.")

    def tablo_olustur(self, db_adi, tablo_adi, sutunlar):
        self.__cursor.execute(f"USE {db_adi}")
        sql = f"CREATE TABLE IF NOT EXISTS {tablo_adi}({sutunlar})ENGINE = InnoDB"
        self.__cursor.execute(sql)
        print(f"'{tablo_adi}' tablosu oluşturuldu.")

    def kullanici_ekle(self, kullanici):
        sql = "INSERT INTO kullanicilar(ad_soyad, mail, telefon, adres) values(%s,%s,%s,%s)"
        self.__cursor.executemany(sql, kullanici)
        self.__connect.commit()
        print(f"{self.__cursor.rowcount} kullanıcı eklendi.")

    def tarife_ekle(self, tarifeler):
        sql = "INSERT INTO tarifeler(tarife, hız_mbps, ücret_azn) values(%s,%s,%s)"
        self.__cursor.executemany(sql, tarifeler)
        self.__connect.commit()
        print(f"{self.__cursor.rowcount} tarife eklendi.")
                
    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connect:
            self.__connect.close()
