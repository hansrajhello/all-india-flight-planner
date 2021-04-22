import json
import pandas as pd
import os

for subdir, dirs, files in os.walk('Schedules'):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".json"):
            # print (filepath)
            try:
                f = open(filepath, "r")
                data = json.loads(f.read())
                f.close()
            except:
                print(Exception)
            
            equipment = data['appendix']['equipments']
            
            if len(equipment):
                
                for eqp in equipment:
                    print(eqp['iata'], end=",")
                    print(eqp['name'])

                