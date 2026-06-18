import requests
import sys
import concurrent.futures

# Signatures indicating a potential subdomain takeover
TAKEOVER_SIGNATURES = {
    "GitHub Pages": "There isn't a GitHub Pages site here.",
    "AWS S3": "NoSuchBucket",
    "Heroku": "herokucdn.com/error-pages/no-such-app.html",
}

def check_subdomain(subdomain):
    subdomain = subdomain.strip()
    # Try HTTPS first, then HTTP
    for scheme in ["https://", "http://"]:
        url = f"{scheme}{subdomain}"
        try:
            response = requests.get(url, timeout=5)
            for provider, signature in TAKEOVER_SIGNATURES.items():
                if signature in response.text:
                    return f"[!] VULNERABLE: {url} ({provider})"
        except requests.exceptions.RequestException:
            continue
    return f"[-] SECURE: {subdomain}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recon_takeover.py <subdomains_file.txt>")
        sys.exit(1)

    print(f"[*] Starting scan...")
    
    with open(sys.argv[1], 'r') as f:
        subdomains = f.readlines()

    # Use ThreadPoolExecutor for faster scanning (10 concurrent threads)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_subdomain, subdomains)
        
    for result in results:
        print(result)
