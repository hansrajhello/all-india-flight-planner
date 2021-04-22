import requests
import pandas as pd
import json
import os
os.chdir("c:/Users/Hansu/Desktop/All Airports Mapping Project")

airports = pd.read_csv('indianairports.csv')
i = 1
date = "2021/05/10"
def getSchedules(a, b):
    
    if a == b:
        return 
    URL = "https://api.flightstats.com/flex/schedules/rest/v1/json/from/"+a+"/to/"+b+"/departing/"+date+"?appId=cc2923d5&appKey=ac2cd1f3256576ec2721ab46b4a179d4"

    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()

    return data

for index1, airport1 in airports.iterrows():
    for index2, airport2 in airports.iterrows():

        print (i)
        i = i+1
            
        code1 = airport1['iata']
        code2 = airport2['iata']
        if code1 == code2:
            continue
        scd = getSchedules(code1, code2)

        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Schedules"
        filename = code1 + code2 + "10052021.json"
        filepath = os.path.join(here, subdir, filename)
        
        f = open(filepath, "w")
        f.write(json.dumps(scd))
        f.close