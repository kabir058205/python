import sys
import time
import pandas as pd
from datetime import datetime
import requests


ENDPOINTS = [
    "https://ifsc.razorpay.com/{}",
    "https://ifsc.bankifsccode.com/{}"
]


def fetch_ifsc(ifsc):
    for url in ENDPOINTS:
        for attempt in range(3):
            try:
                r = requests.get(url.format(ifsc), timeout=5)
                if r.status_code == 200:
                    return r.json()
            except requests.RequestException:
                time.sleep(2 ** attempt)
    return None


def normalize(data, ifsc):
    return {
        "IFSC": data.get("IFSC", ifsc),
        "Bank": data.get("BANK", "N/A"),
        "Branch": data.get("BRANCH", "N/A"),
        "State": data.get("STATE", "N/A"),
        "Timestamp": datetime.now().isoformat()
    }


def save_csv(record, file="IFSC_CODE.csv"):
    df_new = pd.DataFrame([record])
    try:
        df_old = pd.read_csv(file)
        df = pd.concat([df_old, df_new], ignore_index=True)
    except FileNotFoundError:
        df = df_new

    df.to_csv(file, index=False)


def main():

    ifsc = sys.argv[1] if len(sys.argv) > 1 else "SBIN0000001"

    data = fetch_ifsc(ifsc)
    record = normalize(data or {}, ifsc)
    save_csv(record)

    print("IFSC saved:", record)


if __name__ == "__main__":
    main()
