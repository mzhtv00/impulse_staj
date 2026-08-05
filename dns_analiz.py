import dns.resolver

def dns_analizi(domain):
    print("     DNS KAYIT ANALİZİ")
    kayit_turleri = ["A", "MX", "NS", "TXT"]
    for kayit in kayit_turleri:
        print(f"\n{kayit} Kayıtları:")
        try:
            yanitlar = dns.resolver.resolve(domain, kayit)
            for yanit in yanitlar:
                print(f"- {yanit.to_text()}")
        except dns.resolver.NoAnswer:
            print("Kayıt Bulunamadı")
        except dns.resolver.NXDOMAIN:
            print("Domain Bulunamadı")
            break
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    hedef = input("Hedef Domain: ").strip()
    dns_analizi(hedef)
