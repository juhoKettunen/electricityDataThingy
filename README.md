# electricityDataThingy
Simple program for getting electricity consumption data in Finland from Fingrid's api. The main function as a simple UI to get the data which calls the getElectricityConsumptionData function which takes start and end dates and gets the data for each hour between those two days excluding the end date. It also has date checking utils to make sure the dates are valid for api call.

The program requires api key from Fingrid. Guide to get your own key is at https://data.fingrid.fi/en/instructions
Then just put the api key in a .env file as API-KEY="<insert your api key>"
All python library requiremnts are in the requiremnts.txt file.

To run the program you need to clone the repo. Then just call in the folder you cloned it to: python totalElectricityConsumption.py

Example run:

python totalElectricityConsumption.py

Enter start date (YYYY-MM-DD) or 'exit' to quit: 2026-01-01

Enter end date (YYYY-MM-DD): 2026-01-02

Day: 2026-01-01 /// Hour: 00 /// Consumption: 8123704.393 KWh

Day: 2026-01-01 /// Hour: 01 /// Consumption: 8102764.708 KWh

Day: 2026-01-01 /// Hour: 02 /// Consumption: 8030079.946 KWh

Day: 2026-01-01 /// Hour: 03 /// Consumption: 8114975.161 KWh

... and so on
