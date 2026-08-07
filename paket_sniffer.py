from scapy.all import ICMP, IP, TCP, UDP, sniff

def paket_analiz(paket):
    if IP in paket:
        ip_src = paket[IP].src
        ip_dst = paket[IP].dst
        if TCP in paket:
            proto = f"TCP ({paket[TCP].sport} -> {paket[TCP].dport})"
        elif UDP in paket:
            proto = f"UDP ({paket[UDP].sport} -> {paket[UDP].dport})"
        elif ICMP in paket:
            proto = "ICMP (ping)"
        else:
            proto = f"Diğer (Proto ID: {paket[IP].proto})"
        print(f"[{proto:<25}] {ip_src:<15} -> {ip_dst:<15}")

def paket_dinleme(paket_sayisi = 10):
    print(f"    SNIFFER\nPaket sayisi: {paket_sayisi}")
    print("Ağ kartı dinleniyor..\n")
    try:
        sniff(prn = paket_analiz, count = paket_sayisi, store = False)
        print("\nPaketler yakalandı ve analiz edildi\n")
    except PermissionError:
        print("YETKİNİZ YOK. TERMİNALİ YÖNETİCİ OLARAK BAŞLATIN.")
    except Exception as e:
        print(f"Paket yakalanamadı: {e}")

if __name__ == "__main__":
    paket_dinleme()