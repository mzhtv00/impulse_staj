import os
import csv
import uuid
import pandas as pd
from datetime import datetime

def csv_kontrol():
    if not os.path.exists("kullanicilar.csv"):
        with open("kullanicilar.csv", "w", newline = "", encoding = "utf-8") as f:
            yaz = csv.writer(f)
            yaz.writerow(["Ad Soyad", "Id"])

def log_kontrol():
    with open("log_dosyasi.csv", "w", newline = "", encoding = "utf-8") as l:
        with open("log_dosyasi.csv", "a", newline = "", encoding = "utf-8") as l:
            yaz = csv.writer(l)

def log_kayit(funk):
    def wrapper(adsoyad):
        log_kontrol()
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sonuc = funk(adsoyad)
        with open("log_dosyasi.csv", "a", encoding = "utf-8") as l:
            l.write(f"Kullanıcı Kayıt Oldu: {adsoyad}, Tarih: {tarih}")
        return sonuc
    return wrapper

def log_sil(funk):
    def wrapper():
        log_kontrol()
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sonuc = funk()
        with open("log_dosyasi.csv", "a", encoding = "utf-8") as l:
            l.write(f"Kullanıcı silindi: {adsoyad}, Tarih: {tarih}")
        return sonuc
    return wrapper

@log_kayit
def kayit(adsoyad):
    csv_kontrol()

    id = str(uuid.uuid1())[:8]
    kaydet = pd.DataFrame({"Ad Soyad": [adsoyad], "Id": [id]})
    df = pd.read_csv("kullanicilar.csv")
    df = pd.concat([df, kaydet], ignore_index = True)
    df.to_csv("kullanicilar.csv", index = False, encoding = "utf-8")
    print(f"{adsoyad} kaydedildi\nID'niz: {id}\n")
    return id

@log_sil
def sil():
    csv_kontrol()

    df = pd.read_csv("kullanicilar.csv")
    if df.empty:
        print("Dosya boş")
        return
    id = input("Silmek istediğiniz ID: ")
    if id not in df["Id"].values:
        print("ID bulunamadı")
        return
    silinen = df[df["Id"] == id]["Ad Soyad"].values[0]
    df = df[df["Id"] != id]
    df.to_csv("kullanicilar.csv", index = False, encoding = "utf-8")
    print(f"{silinen} silindi\n")

if __name__ == "__main__":
    while True:
        print("""\n1. Kullanıcı Kayıt\n2. Kullanıcı Sil\n3. Çıkış\n""")
        sec = input("İşlem seçin: ")
        if sec == "1":
            adsoyad = input("Ad Soyad: ")
            kayit(adsoyad)
        elif sec == "2":
            sil()
        elif sec == "3":
            break
        else:
            print("Geçersiz seçim")
