import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create output folder
os.makedirs("data", exist_ok=True)

# Define start and end dates
start_date = datetime.strptime("202404", "%Y%m")
end_date = datetime.strptime("202505", "%Y%m")

# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://www.bom.gov.au/"
}

# Loop over each month
current_date = start_date
while current_date <= end_date:
    yyyymm = current_date.strftime("%Y%m")
    url = f"http://www.bom.gov.au/climate/dwo/{yyyymm}/text/IDCJDW2124.{yyyymm}.csv"
    output_path = os.path.join("data", f"IDCJDW2124.{yyyymm}.csv")

    print(f"Downloading: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for 4xx/5xx responses
        with open(output_path, "wb") as f:
            f.write(response.content)
    except requests.HTTPError as e:
        print(f"Failed to download {yyyymm}: {e}")
    except Exception as e:
        print(f"Error for {yyyymm}: {e}")

    # Move to next month
    current_date += relativedelta(months=1)
