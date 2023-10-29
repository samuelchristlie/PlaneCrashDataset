import requests
from lxml import html
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import re
from datetime import datetime

from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="Research")

crashes = []
columns = ["Year", "Month", "Day", "Time", "LocationRaw", "Location", "Lat", "Long", "Country", "Operator", "FlightNo", 
           "Route", "ACType", "Registration", "CNLN", "AboardPassengers", "AboardCrew", "FatalitiesPassengers",
           "FatalitiesCrew", "Ground", "Summary"]

for pageyear in range(1920, 2023+1):
    i = 1

    content = requests.get(f"https://www.planecrashinfo.com/{pageyear}/{pageyear}-{i}.htm").content
    while html.fromstring(content).xpath("/html/head/title") == []:
        # Uncomment to see progress
        # print(f"{pageyear}-{i}")

        date = parse(html.fromstring(content).xpath("/html/body/div/center/table/tr[2]/td[2]/font/text()")[0])
        year = date.year
        month = date.month
        day = date.day
        
        time = None
        try:
            time = datetime.strptime(html.fromstring(content).xpath("/html/body/div/center/table/tr[3]/td[2]/font/text()")[0], '%H%M').time()
        except:
            pass

        locationraw = html.fromstring(content).xpath("/html/body/div/center/table/tr[4]/td[2]/font/text()")[0]

        lat = None
        lng = None
        country = None
        # countrylat = None
        # countrylng = None

        try:
            geocoded = geocoder.geocode(locationraw, exactly_one=True, addressdetails=True, language='en').raw
            location = geocoded["display_name"]
            lat = geocoded["lat"]
            lng = geocoded["lon"]
            country = geocoded["address"]["country"]

            # if country:
            #     countrygeocoded = geocoder.geocode(geocoder.geocode(country, exactly_one=True, addressdetails=True, language='en').raw["address"]["country"], exactly_one=True, addressdetails=True, language='en').raw
            #     countrylat = countrygeocoded["lat"]
            #     countrylng = countrygeocoded["lon"]

        except:
            pass
        
        operator = html.fromstring(content).xpath("/html/body/div/center/table/tr[5]/td[2]/font/text()")[0]
        flightno = html.fromstring(content).xpath("/html/body/div/center/table/tr[6]/td[2]/font/text()")[0]
        route = html.fromstring(content).xpath("/html/body/div/center/table/tr[7]/td[2]/font/text()")[0]
        actype = html.fromstring(content).xpath("/html/body/div/center/table/tr[8]/td[2]/font/text()")[0]
        registration = html.fromstring(content).xpath("/html/body/div/center/table/tr[9]/td[2]/font/text()")[0]
        cnln = html.fromstring(content).xpath("/html/body/div/center/table/tr[10]/td[2]/font/text()")[0]

        aboard = html.fromstring(content).xpath("/html/body/div/center/table/tr[11]/td[2]/font/text()")[0]
        searchaboardpassengers = re.search(r'passengers:(\d+)', aboard) 
        aboardpassengers = int(searchaboardpassengers.group(1)) if searchaboardpassengers else None

        searchaboardcrew = re.search(r'crew:(\d+)', aboard)
        aboardcrews = int(searchaboardcrew.group(1)) if searchaboardcrew else None

        fatalities = html.fromstring(content).xpath("/html/body/div/center/table/tr[12]/td[2]/font/text()")[0]
        searchfatalitiespassengers = re.search(r'passengers:(\d+)', fatalities) 
        fatalitiespassengers = int(searchfatalitiespassengers.group(1)) if searchfatalitiespassengers else None

        searchfatalitiescrew = re.search(r'crew:(\d+)', fatalities)
        fatalitiescrews = int(searchfatalitiescrew.group(1)) if searchfatalitiescrew else None

        ground = None

        try:
            ground = int(html.fromstring(content).xpath("/html/body/div/center/table/tr[13]/td[2]/font/text()")[0])
        except:
            pass


        summary = html.fromstring(content).xpath("/html/body/div/center/table/tr[14]/td[2]/font/text()")[0]

        row = [year, month, day, time, locationraw, location, lat, lng, country, operator, flightno, route,
               actype, registration, cnln, aboardpassengers, aboardcrews, fatalitiespassengers, fatalitiescrews, ground, summary]

        crashes.append(row)
  

        i += 1
        content = requests.get(f"https://www.planecrashinfo.com/{pageyear}/{pageyear}-{i}.htm").content


df = pd.DataFrame(crashes, columns=columns)
df.to_csv("planeCrashes.csv", index=False)
# Uncomment to see result
# df
