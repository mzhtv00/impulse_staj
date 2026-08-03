import sys
import time

try:
    from hiz_testi import hiz_testi_log
    from isp_kontrol import bilgi_al
    from ping_izleyici import baslat
    from port_tarayici import port_taramasi_yap, yerel_ip_al
except ImportError as e:
    print(f"Modül bulunamadı: {e}")
    sys.exit()


def ana_menu():
    while True:
        print("\nWI-FI AĞ ANALİZ ARAÇ SETİ\n")
        print("1. Ağ Bağlantısı ve Ping İzleyici")
        print("2. Dış IP ve ISP Bilgisi")
        print("3. İnternet Hız Testi")
        print("4. Port Tarayıcı")
        print("0. Çıkış")

        sec = input("İşlem Seçin: ").strip()

        if sec == "1":
            hedef = (input("Ping Atılacak IP (Varsayılan: 8.8.8.8): ").strip() or "8.8.8.8")
            print("\nİzleme Başlatılıyor..")
            time.sleep(1)
            baslat(hedef_ip = hedef)

        elif sec == "2":
            bilgi_al()
            input("\nDevam etmek için Enter'a basın")

        elif sec == "3":
            hiz_testi_log()
            input("\nDevam etmek için Enter'a basın")

        elif sec == "4":
            kendi_ip = yerel_ip_al()
            hedef_ip = (input(f"Taranacak IP (Varsayılan: {kendi_ip}): ").strip() or kendi_ip)
            test_portlari = [21, 22, 80, 443, 8080, 3389]
            port_taramasi_yap(hedef_ip, test_portlari)
            input("\nDevam etmek için Enter'a basın")

        elif sec == "0":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz giriş")
            time.sleep(1)

if __name__ == "__main__":
    ana_menu()