import time
import requests
from datetime import datetime, timedelta
from tqdm import tqdm

def generate_dates(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    delta = end_date - start_date

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        yield date.strftime("%m/%d/%Y")

url = "https://ctf.cyber-cit.club/api/v1/challenges/attempt"
cookies = {"session": ""}             <------------------------------7OT COOKIES HNA
headers = {
    "Content-Type": "application/json",
    "Csrf-Token": ""                <------------------------------7OT CSRF token HNA
}

start_year = 2000                   <------------------------------7OT start date HNA
end_year = 2015                     <------------------------------7OT end date HNA

total_days = (datetime(end_year, 12, 31) - datetime(start_year, 1, 1)).days + 1

for date in tqdm(generate_dates(start_year, end_year), total=total_days, desc="Testing dates"):
    payload = {
        "challenge_id": 69,
        "submission": f"CIT{{{date}}}"
    }

    response = requests.post(url, json=payload, cookies=cookies, headers=headers)
    data = response.json()

    if data.get("data", {}).get("status") != "incorrect":
        print(f"\nFound potential match: CIT{{{date}}}")
        print("Response:", data)
        time.sleep(120)
    time.sleep(9)