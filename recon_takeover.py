import requests
import sys

TAKEOVER_SIGNATURES = {
    "GitHub Pages": "There isn't a GitHub Pages site here.",
    "AWS S3": "NoSuchBucket",
    "Heroku": "herokucdn.com/error-pages/no-such-app.html",
}

def check_subdomain(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url, timeout=5)
        for provider, signature in TAKEOVER_SIGNATURES.items():
            if signature in response.text:
                return f"[!] POTENTIAL TAKEOVER FOUND: {subdomain} ({provider})"
    except requests.exceptions.RequestException:
        return f"[-] Could not connect to {subdomain}"
    return f"[+] {subdomain} is secure."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python recon_takeover.py <plik_z_subdomenami.txt>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print(check_subdomain(line.strip()))
