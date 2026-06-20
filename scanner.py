import socket
import sys

def scan_subdomains(domain, wordlist):
    print(f"\n[+] Scanning subdomains for: {domain}\n")

    try:
        with open(wordlist, "r") as file:
            subdomains = file.read().splitlines()

        for subdomain in subdomains:
            full_domain = f"{subdomain}.{domain}"

            try:
                ip = socket.gethostbyname(full_domain)
                print(f"[FOUND] {full_domain} --> {ip}")

            except socket.gaierror:
                pass

    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        sys.exit()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python scanner.py example.com")
        sys.exit()

    target_domain = sys.argv[1]

    scan_subdomains(target_domain, "subdomains.txt")