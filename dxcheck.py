#!/usr/bin/env python3
import urllib.request
import re

URL = "https://services.swpc.noaa.gov/text/wwv.txt"

def classify(sfi, k):
    if k >= 4: return "\033[91mROSSZ (Vihar)\033[0m"
    if sfi >= 150: return "\033[92mKIVÁLÓ (DX)\033[0m"
    if sfi >= 100: return "\033[93mJÓ\033[0m"
    return "\033[33mGYENGE\033[0m"

try:
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as r:
        text = r.read().decode('utf-8')

    # Javított keresés: csak a számokat és a tizedespontot vesszük ki, a mondatzáró pontot nem
    sfi_match = re.search(r"Solar flux\s+(\d+)", text)
    # Itt a [\d\.]+ utáni rész biztosítja, hogy ne ragadjon be a mondatvégi pont
    k_match = re.search(r"planetary K-index.*?was\s+([\d\.]+)", text)
    a_match = re.search(r"planetary A-index\s+(\d+)", text)

    if sfi_match and k_match:
        sfi = int(sfi_match.group(1))
        # A strip('.') eltávolítja a mondatvégi pontot, ha mégis bekerülne
        k_str = k_match.group(1).rstrip('.')
        k = float(k_str)
        a_index = a_match.group(1) if a_match else "?"

        print(f"\n--- 11m / CB AKTUÁLIS ADATOK ---")
        print(f"Solar Flux (SFI): {sfi}")
        print(f"K-index:          {k}")
        print(f"A-index:          {a_index}")
        print(f"Terjedés:         {classify(sfi, k)}")
        print(f"---------------------------------\n")
    else:
        print("Hiba: Nem találom a számokat a szövegben.")

except Exception as e:
    print(f"Hiba történt: {e}")
