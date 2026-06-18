# SubTakeover Scanner 🛡️

Lekkie narzędzie do automatycznego wykrywania błędnych konfiguracji DNS (dangling DNS), które mogą prowadzić do przejęcia subdomeny (Subdomain Takeover).

## Funkcje
- [x] Szybkie skanowanie listy subdomen.
- [x] Wykrywanie błędów dla AWS S3, GitHub Pages i Heroku.
- [x] Łatwa integracja z pipeline'ami CI/CD.

## Instalacja
```bash
git clone [https://github.com/twoja-organizacja/sub-takeover-scanner.git](https://github.com/twoja-organizacja/sub-takeover-scanner.git)
cd sub-takeover-scanner
pip install -r requirements.txt
