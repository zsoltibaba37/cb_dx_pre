#!/usr/bin/env python3
import urllib.request

URL = "https://services.swpc.noaa.gov/text/daily-solar-indices.txt"

RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
RESET  = "\033[0m"

def classify(flux, ssn):
    if flux >= 150 and ssn >= 100:
        return GREEN, "KIVÁLÓ"
    elif flux >= 120 and ssn >= 50:
        return YELLOW, "JÓ"
    else:
        return RED, "GYENGE"

with urllib.request.urlopen(URL) as r:
    for line in r.read().decode().splitlines():
        if line.startswith("#") or line.startswith(":") or not line.strip():
            print(line)
            continue
        parts = line.split()
        try:
            flux = int(parts[3])
            ssn  = int(parts[4])
            color, label = classify(flux, ssn)
            print(f"{color}{line}  <- {label}{RESET}")
        except:
            print(line)
