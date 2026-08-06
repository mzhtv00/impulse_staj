import platform
import subprocess


def domain_temizle(domain):
    domain = domain.strip().lower()
    if domain.startswith("https://"):
        domain = domain[8:]
    elif domain.startswith("http://"):
        domain = domain[7:]
    if "/" in domain:
        domain = domain.split("/")[0]
    return domain

def calistir(hedef, max_hop = 15):
    temiz_hedef = domain_temizle(hedef)
    sistem = platform.system().lower()
    print("\n     AĞ ROTASI İZLEME\n")
    if sistem == "windows":
        komut = ["tracert", "-h", str(max_hop), temiz_hedef]
    else:
        komut = ["traceroute", "-m", str(max_hop), temiz_hedef]
    try:
        process = subprocess.Popen(komut,
                                   stdout = subprocess.PIPE,
                                   stderr = subprocess.STDOUT,
                                   text = True,
                                   encoding = "cp857" 
                                   if sistem == "windows" 
                                   else "utf-8", 
                                   errors = "ignore",
                                   )
        for satir in process.stdout:
            satir_temizle = satir.strip()
            if satir_temizle:
                print(satir_temizle)
        process.wait()
    except Exception as e:
        print(f"\nTraceroute çalıştırma başarısı: {e}\n")

if __name__ == "__main__":
    hedef = (input("Hedef Domain veya IP (Varsayılan: google.com): ").strip() or "google.com")
    calistir(hedef)