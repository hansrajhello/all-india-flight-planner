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

# Set center for our map
center = [23.677955, 78.778878]
# initialize map with center and zoom
map_india = folium.Map(location=center, zoom_start=5)

# look up in cached responses for no. of Flights
def noOfFlightsBetween(fromAirport, toAirport):
    
    if fromAirport == toAirport:
        return 'N'
    
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


for i in range(0, len(airports)):
    for j in range(i+1, len(airports)):   
        code1 = airports.iloc[i]['iata']
        code2 = airports.iloc[j]['iata']
        name1 = airports.iloc[i]['name']
        name2 = airports.iloc[j]['name']
        city1 = airports.iloc[i]['city']
        city2 = airports.iloc[j]['city']
        color = airports.iloc[i]['region']
        # print("Test - ", airports.iloc[i]['iata'], airports.iloc[j]['iata'])        
        location1 = [airports.iloc[i]['latitude'], airports.iloc[i]['longitude']]
        location2 = [airports.iloc[j]['latitude'], airports.iloc[j]['longitude']]
        folium.Marker(
            location1, tooltip=f'{city1}:{name1}', icon=folium.Icon(color=f'{color}',prefix='fa',icon='bookmark')).add_to(map_india)
        
        if code1 == code2:
            continue
            
        # call above defined function
        # TODO: call noOfFlightsBetween() in BOTH DIRECTIONS
        flights1 = noOfFlightsBetween(code1, code2)
        flights2 = noOfFlightsBetween(code2, code1)
        
        if flights1 == 0 & flights2 == 0:
            print("No Flights between ", code1, code2)
            continue
        print(flights1, "Flights from", code1, "-", code2, end=", ")
        print(flights2, "from", code2, "-", code1)
        
        # clear array contents
        points = []
        points.append(tuple(location1))
        points.append(tuple(location2))
        # draw lines among given points
        folium.PolyLine(points, color=f'{color}',tooltip=f'{city1}-{city2} {flights1}\n{city2}-{city1} {flights2}',weight=7, opacity=0.5).add_to(map_india)
        # folium.PolyLine(points, color="red", popup=f'From:{airport1["iata"]}\n To:{code2}',weight=10, opacity=0.5).add_to(map_india)

# save map to html file
map_india.save('purple_hansu_max_pro.html')