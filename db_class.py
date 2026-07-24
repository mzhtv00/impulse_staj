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

    def insert_record(self, tablo_adi, veri):
        sutunlar = ", ".join(veri.keys())
        values = tuple(veri.values())
        placeholders = ", ".join(["%s"] * len(veri))
        sql = f"INSERT INTO {tablo_adi}({sutunlar}) values({placeholders})"
        self.__cursor.executemany(sql, values)
        self.__connect.commit()

    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connect:
            self.__connect.close()
