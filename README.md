# SubTakeover Scanner 🛡️

A lightweight, modular scanner designed to automatically identify dangling DNS records that may be susceptible to **Subdomain Takeover**.

## Features
- [x] Fast scanning of custom subdomain lists.
- [x] Detection of common misconfigurations for AWS S3, GitHub Pages, and Heroku.
- [x] Easy integration into CI/CD pipelines.

## Installation

```bash
# Clone the repository
git clone https://github.com/RisetrokPTT/subdomain-takeover-scanner.git

# Enter the directory
cd subdomain-takeover-scanner

# Install dependencies
pip install -r requirements.txt
```

##Usage
    Create a file named subdomains.txt and add your subdomains (one per line):
    dev.example.com
    test.example.com
    Run the script using Python:

    python recon_takeover.py subdomains.txt

The script will output the results directly to the terminal, highlighting any potential takeover vulnerabilities found.

##Contributing

  Contributions are welcome! If you find a bug or want to add support for new services, feel free to open an Issue or submit a Pull Request.
  
##License

  This project is licensed under the MIT License. See the LICENSE file for details.
  
##Disclaimer

  This tool is for educational purposes and authorized security testing only. The author is not responsible for any misuse or damage caused by this tool. Only use this scanner on targets you have explicit permission to test.
  
