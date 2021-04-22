import folium
import json
import requests
import pandas as pd
import os

# TODO: Don't use hardcoded date

# Was having trouble opening indiansairports.csv
os.chdir("c:/Users/Hansu/Desktop/All Airports Mapping Project")

airports = pd.read_csv('indianairports.csv')
# view the dataset
# print(airports.head())

# look up in cached responses for no. of Flights
def noOfFlightsBetween(fromAirport, toAirport):
    
    if fromAirport == toAirport:
        return 0
    
    # open targeted file
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Schedules"
    filename = fromAirport + toAirport + "10052021.json"
    filepath = os.path.join(here, subdir, filename)
    
    try:
        f = open(filepath, "r")
        data = json.loads(f.read())
        f.close()
    except:
        return 0
    
    scheduled = data['scheduledFlights']  

    # return no. of flights between given airports on given date
    return len(scheduled)

print("H",end=",")
for i in range(0, len(airports)):
    name1 = airports.iloc[i]['name']
    print(name1, end=",")
print("H")
print("H",end=",")
for i in range(0, len(airports)):
    code1 = airports.iloc[i]['iata']
    name1 = airports.iloc[i]['name']
    city1 = airports.iloc[i]['city']
    print(city1, end=",")
print("H")
print("H",end=",")
for i in range(0, len(airports)):
    code1 = airports.iloc[i]['iata']
    name1 = airports.iloc[i]['name']
    city1 = airports.iloc[i]['city']
    print(code1, end=",")
print("H")
for i in range(0, len(airports)):
    code1 = airports.iloc[i]['iata']
    name1 = airports.iloc[i]['name']
    city1 = airports.iloc[i]['city']
    print(name1, end=",")
    print(city1, end=",")
    print(code1, end=",")
    for j in range(0, len(airports)):   
        code2 = airports.iloc[j]['iata']
        name2 = airports.iloc[j]['name']
        city2 = airports.iloc[j]['city']
        
        # call above defined function
        # TODO: call noOfFlightsBetween() in BOTH DIRECTIONS
        flights1 = noOfFlightsBetween(code1, code2)
        
        print(flights1, end=",")
    print("H")