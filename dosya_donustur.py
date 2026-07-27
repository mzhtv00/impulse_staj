import json
import xmltodict
import pandas as pd
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

def json_donustur_csv():
    json_dosyasi = input("Json dosya yolunu girin: ")
    csv_dosyasi = input("Oluşturulacak csv dosyasının adı(.csv): ")
    df = pd.read_json(json_dosyasi)
    df.to_csv(csv_dosyasi, index = False, encoding = "utf-8")
    print(f"Json Csv'ye dönüştürüldü: {csv_dosyasi}")

def json_donustur_xml():
    json_dosyasi = input("Json dosya yolunu girin: ")
    xml_dosyasi = input("Oluşturulacak xml dosyasının adı(.xml): ")
    with open(json_dosyasi, "r", encoding = "utf-8") as f:
        veri = json.load(f)
    donustur = dicttoxml(veri, custom_root = "root", attr_type = False)
    dom = parseString(donustur)
    temiz_xml = dom.toprettyxml(encoding = "utf-8")
    with open(xml_dosyasi, "wb") as f:
        f.write(temiz_xml)
    print(f"Json Xml'e dönüştürüldü: {xml_dosyasi}")

def xml_donustur_csv():
    xml_dosyasi = input("Xml dosya yolunu girin: ")
    csv_dosyasi = input("Oluşturulacak csv dosyasının adı(.csv): ")
    df = pd.read_xml(xml_dosyasi)
    df.to_csv(csv_dosyasi, index = False, encoding = "utf-8")
    print(f"Xml Csv'ye dönüştürüldü: {csv_dosyasi}")

def xml_donustur_json():
    xml_dosyasi = input("Xml dosya yolunu girin: ")
    json_dosyasi = input("Oluşturulacak json dosyasının adı(.json): ")
    with open(xml_dosyasi, "r", encoding = "utf-8") as f:
        icerik = f.read()
    veri = xmltodict.parse(icerik)
    with open(json_dosyasi, "w", encoding = "utf-8") as f:
        json.dump(veri, f, ensure_ascii = False, indent = 4)
    print(f"Xml Json'a dönüştürüldü: {json_dosyasi}")

if __name__ == "__main__":
    while True:
        print("\n1. Json'u Csv'ye dönüştür\n2. Json'u Xml'e dönüştür\n3. Xml'i Csv'ye dönüştür\n4. Xml'i Json'a dönüştür\n5. Çıkış\n")
        try:
            choice = int(input("İşlem seçin: "))
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue
        if choice == 1:
            json_donustur_csv()
        elif choice == 2:
            json_donustur_xml()
        elif choice == 3:
            xml_donustur_csv()
        elif choice == 4:
            xml_donustur_json()
        elif choice == 5:
            print("Çıkış yapılıyor..")
            break
        else:
            print("Geçersiz işlem.")
