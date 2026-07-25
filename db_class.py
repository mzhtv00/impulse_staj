import mysql.connector


class MySqlDB:
    def __init__(self): # <-- database eklenebilir
        self.__host =  "localhost"
        self.__user = "root"
        self.__password = "root"
        self.__connect = None
        self.__cursor = None

    def connect(self, database = None):
        self.__connect = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = database
        )
        if self.__connect.is_connected():
            self.__cursor = self.__connect.cursor(buffered = True)
            print("Bağlantı başarılı.")
        else:
            print("Bağlantı başarısız.")

    def db_olustur(self, db_adi, charset = "utf8mb4", collation = "utf8mb4_0900_ai_ci"):
        sql = f"CREATE DATABASE IF NOT EXISTS {db_adi} CHARACTER SET {charset} COLLATE {collation}"
        self.__cursor.execute(sql)
        print(f"'{db_adi}' database'i oluşturuldu.")

    def tablo_olustur(self, tablo_adi, sutunlar):
        sql = f"CREATE TABLE IF NOT EXISTS {tablo_adi}({sutunlar})ENGINE = InnoDB"
        self.__cursor.execute(sql)
        print(f"'{tablo_adi}' tablosu oluşturuldu.")

    def insert_record(self, tablo_adi, veri):
        sutunlar = ", ".join(veri.keys())
        values = tuple(veri.values())
        placeholders = ", ".join(["%s"] * len(veri))
        sql = f"INSERT INTO {tablo_adi}({sutunlar}) values({placeholders})"
        self.__cursor.execute(sql, values)
        self.__connect.commit()

    def insert_ignore(self, tablo_adi, veri):
        sutunlar = ", ".join(veri.keys())
        values = tuple(veri.values())
        placeholders = ", ".join(["%s"] * len(veri))
        sql = f"INSERT IGNORE INTO {tablo_adi}({sutunlar}) values({placeholders})"
        self.__cursor.execute(sql, values)
        self.__connect.commit()

    def get_rows(self, sql, params = None):
        self.__cursor.execute(sql, params or ())
        return self.__cursor.fetchall()

    def get_row(self, sql, params = None):
        self.__cursor.execute(sql, params or ())
        return self.__cursor.fetchone()

    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connect:
            self.__connect.close()
