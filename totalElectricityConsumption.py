import urllib.request, json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
apiKey = os.getenv("API-KEY")

maxHours = 744  # Maximum hours in a month

def parseDate(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format; expected YYYY-MM-DD")

def validateDates(start, end):
    s = parseDate(start)
    e = parseDate(end)
    today = datetime.now().date()
    if s > today or e > today:
        raise ValueError("Dates cannot be in the future")
    if e < s:
        raise ValueError("End date must be the same or after start date")
    return s, e

def daysBetween(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")

    delta = (d2 - d1).days
    if delta < 0:
        raise ValueError("End date must be the same or after start date")
    return delta

def getElectricityConsumption(start="2026-01-01", end="2026-01-02"):
    try:

        validateDates(start, end)
        hours = daysBetween(start, end) * 24

        if hours == 0:
            hours = 24
        elif hours > maxHours:
            hours = maxHours

        url = f"https://data.fingrid.fi/api/datasets/363/data?startTime={start}&endTime={end}&format=json&oneRowPerTimePeriod=true&pageSize={hours}&locale=en&sortBy=startTime"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'x-api-key': apiKey,
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)

        data = json.loads(response.read())['data']

        for entry in data:
            day = entry['startTime'].split('T')[0]
            hour = entry['startTime'].split('T')[1].split(':')[0]
            consumption = entry['Total electricity consumption in Finnish distribution networks']
            print(f"Day: {day} /// Hour: {hour} /// Consumption: {consumption} KWh")

    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        start_date = input("Enter start date (YYYY-MM-DD) or 'exit' to quit: ")
        if start_date.lower() == 'exit':
            break
        end_date = input("Enter end date (YYYY-MM-DD): ")
        getElectricityConsumption(start=start_date, end=end_date)

if __name__ == "__main__":
    main()