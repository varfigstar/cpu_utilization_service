import time
from argparse import ArgumentParser

import psutil
import requests


parser = ArgumentParser()
parser.add_argument("--interval", default=5)
parser.add_argument("--URL", default="http://localhost:8000")

args = parser.parse_args()
interval = int(args.interval)
BACKEND_URL = args.URL


def main():
    start = time.time()
    while True:
        if time.time() - start < interval:
            continue
        cpu_utilization = psutil.cpu_percent()
        r = requests.post(f"{BACKEND_URL}/api/cpu_info/", data={"utilization_percent": cpu_utilization})
        print(r.json())


if __name__ == "__main__":
    main()



