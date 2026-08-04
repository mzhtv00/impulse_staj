import subprocess


def wifi_tarama():
    try:
        raw_if = subprocess.check_output(
            "netsh wlan show interfaces", shell=True
        ).decode("cp857", errors="ignore")
        if_veri = {}
        for line in raw_if.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                if_veri[k.strip().lower()] = v.strip()
        durum = if_veri.get("durum", if_veri.get("state", "Bilinmiyor"))
        bagli_ssid = if_veri.get("ssid", "Bağlı Değil")
        bagli_sinyal = if_veri.get(
            "sinyal", if_veri.get("signal", "Bilinmiyor")
        )
        guvenlik = if_veri.get(
            "kimlik doğrulama", if_veri.get("authentication", "Bilinmiyor")
        )
        print("                   BAĞLI WI-FI BİLGİSİ")
        print(f"Durum          : {durum}")
        print(f"Bağlı SSID     : {bagli_ssid}")
        print(f"Sinyal Kalitesi: {bagli_sinyal}")
        print(f"Güvenlik Türü  : {guvenlik}\n")
    except Exception as e:
        print(f"Bağlı ağ bilgisi alınamadı: {e}")

    try:
        raw_net = subprocess.check_output(
            "netsh wlan show networks mode=bssid", shell=True
        ).decode("cp857", errors="ignore")

        print("                   ÇEVREDEKİ WI-FI AĞLARI")
        aglar = []
        mevcut_ag = {}
        for line in raw_net.splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, val = line.split(":", 1)
            key = key.strip().lower()
            val = val.strip()
            if key.startswith("ssid"):
                if mevcut_ag:
                    aglar.append(mevcut_ag)
                    mevcut_ag = {}
                mevcut_ag["ssid"] = val if val else "[Gizli Ağ]"
            elif (
                "kimlik" in key or "authentication" in key or "doğrulama" in key
            ):
                mevcut_ag["guvenlik"] = val
            elif "sinyal" in key or "signal" in key:
                if "sinyal" not in mevcut_ag:
                    mevcut_ag["sinyal"] = val
        if mevcut_ag:
            aglar.append(mevcut_ag)
        if not aglar:
            print("Görünür Wi-Fi ağı bulunamadı.")
        else:
            print(f"{'SSID':<30} | {'Sinyal':<10} | {'Güvenlik':<18}")
            print("-" * 65)
            for ag in aglar:
                s_name = ag.get("ssid", "[Gizli Ağ]")
                s_sig = ag.get("sinyal", "N/A")
                s_sec = ag.get("guvenlik", "Bilinmiyor")
                print(f"{s_name:<30} | {s_sig:<10} | {s_sec:<18}")
    except Exception as e:
        print(f"Çevredeki ağlar taranırken hata oluştu: {e}")

if __name__ == "__main__":
    wifi_tarama()