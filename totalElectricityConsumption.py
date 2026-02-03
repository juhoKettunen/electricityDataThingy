import urllib.request, json
import os
from dotenv import load_dotenv

def getElectricityConsumption():
    try:
        load_dotenv()

        url = "https://data.fingrid.fi/api/datasets/363/data?startTime=2026-01-01&endTime=2026-01-02&format=json&oneRowPerTimePeriod=true&pageSize=24&locale=en&sortBy=startTime"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'x-api-key': os.getenv('API-KEY'),
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        print(response.getcode())
        print(response.read())
    except Exception as e:
        print(e)

def main():
    getElectricityConsumption()

if __name__ == "__main__":
    main()