import json
import uuid
import boto3
import random
import pandas as pd
from faker import Faker

fake = Faker('az_AZ')

class Tarif:
    def __init__(self, tarif_id, tarif_adi, tarif_fiyati, tarif_ozelligi):
        self.tarif_id = tarif_id
        self.tarif_adi = tarif_adi
        self.tarif_fiyati = tarif_fiyati
        self.tarif_ozelligi = tarif_ozelligi

    def to_dict(self):
        return {
            "tarif_id": self.tarif_id,
            "tarif_adi": self.tarif_adi,
            "tarif_fiyati": f"{self.tarif_fiyati} AZN",
            "tarif_ozelligi": self.tarif_ozelligi
        }

class Musteri:
    def __init__(self, musteri_id, musteri_adi_soyadi, musteri_email, musteri_telefon, musteri_adresi, kullandigi_tarif):
        self.musteri_id = musteri_id
        self.musteri_adi_soyadi = musteri_adi_soyadi
        self.musteri_email = musteri_email
        self.musteri_telefon = musteri_telefon
        self.musteri_adresi = musteri_adresi
        self.kullandigi_tarif = kullandigi_tarif

    def to_dict(self):
        return {
            "musteri_id": self.musteri_id,
            "musteri_adi_soyadi": self.musteri_adi_soyadi,
            "musteri_email": self.musteri_email,
            "musteri_telefon": self.musteri_telefon,
            "musteri_adresi": self.musteri_adresi.replace("\n", ", "),
            "tarif_adi": self.kullandigi_tarif.tarif_adi
        }

tarifler = [
    Tarif(1, "Standart", 25, "50 Mbps limitsiz"),
    Tarif(2, "Premium", 50, "200 Mbps limitsiz"),
    Tarif(3, "Business", 90, "500 Mbps limitsiz"),
    Tarif(4, "Ultra", 150, "1 Gbps limitsiz")
]

def temiz_email(isim):
    tr_aze = str.maketrans('əıçşğöü ', 'eicsgou.')
    return f"{isim.lower().translate(tr_aze)}{random.randint(10,999)}@{fake.free_email_domain()}"

def lambda_handler(event, context):
    aboneler_listesi = [
        Musteri(
            musteri_id = str(uuid.uuid4()),
            musteri_adi_soyadi = (isim := fake.name()),
            musteri_email = temiz_email(isim),
            musteri_telefon = fake.phone_number(),
            musteri_adresi = fake.address(),
            kullandigi_tarif = random.choice(tarifler)
        ).to_dict()
        for _ in range(1000)
    ]

    xlsx_dosyasi = '/tmp/aboneler_listesi.xlsx'
    df = pd.DataFrame(aboneler_listesi)
    df.to_excel(xlsx_dosyasi, index=False, engine='openpyxl')

    s3 = boto3.client('s3')
    bucket_adi = 'musteri-olusturma-bucket'
    s3.upload_file(xlsx_dosyasi, bucket_adi, 'aboneler_listesi.xlsx')

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mesaj': f'{len(aboneler_listesi)} abone başarıyla üretildi ve Excel olarak kaydedildi.',
            'dosya_yolu': xlsx_dosyasi
        }, ensure_ascii=False)
    }