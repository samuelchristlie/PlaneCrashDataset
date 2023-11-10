# PlaneCrashDataset
This dataset contains information about plane crashes obtained from the website [planecrashinfo.com](https://planecrashinfo.com/). The data includes details such as the date, location, operator, aircraft type, fatalities, and other relevant information related to each incident, including additional variables. The dataset is automatically updated every month using GitHub actions.

## Dataset Information

The dataset consists of the following columns:

- **Year**: The year in which the plane crash occurred.
- **Month**: The month of the plane crash.
- **Day**: The day of the month on which the plane crash occurred.
- **Time**: The time of the plane crash.
- **LocationRaw**: The raw description of the crash location.
- **Location**: The crash location according to Nominatim, if available
- **Lat**: The latitude of the crash location according to Nominatim, if available
- **Long**: The longitude of the crash location according to Nominatim, if available
- **Country**: The country in which the crash occurred.
- **Operator**: The operator of the aircraft involved in the crash.
- **FlightNo**: The flight number associated with the aircraft.
- **Route**: The route of the flight.
- **ACType**: The type of aircraft involved in the crash.
- **Registration**: The registration number of the aircraft.
- **CNLN**: The constructor number (CN/LN) of the aircraft.
- **AboardPassengers**: The number of passengers aboard the aircraft.
- **AboardCrew**: The number of crew members aboard the aircraft.
- **FatalitiesPassengers**: The number of passenger fatalities.
- **FatalitiesCrew**: The number of crew fatalities.
- **Ground**: The number of ground fatalities.
- **Summary**: A summary of the incident.

## Data Collection

The data is extracted from the website [planecrashinfo.com](https://planecrashinfo.com/), which provides comprehensive information on aviation accidents. The process involved extracting the relevant information from each incident page and organizing it into a structured format using Python. 

## Data Usage

This dataset can be valuable for various purposes, including:

- Analysis of aviation safety and accident patterns.
- Research on factors contributing to plane crashes.
- Statistical modeling and predictive analysis.
- Visualization and storytelling through data.

**Disclaimer**: The dataset is based on publicly available information from [planecrashinfo.com](https://planecrashinfo.com/). I am not responsible for the accuracy or reliability of the data.
