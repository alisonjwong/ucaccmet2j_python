# Part 1
# Find the station code for Seattle

file_name = 'stations.csv'

with open(file_name) as file:
    stations = file.readlines()
 

for line in stations:
    location, state, station_code = line.strip().split(',') 
    if location == 'Seattle': 
        seattle_code = station_code 
    # stations.append({'Location': location, 'State': state, 'Station code': station_code})

print(seattle_code)

# Select all the measurements belonging to it from JSON data.

import json

with open ('precipitation.json') as file:
    precipitation = json.load(file)
    seattle_prec = []
    for i in range(len(precipitation)):
        if precipitation [i]['station'] == seattle_code:
            seattle_prec.append({'Date': precipitation[i]['date'], 'Value': precipitation[i]['value']})

# Sum all the measurement for that location for each month


total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

for measurement in precipitation:
    if 'GHCND:US1WAKG0038' in measurement ['station']:
        print(measurement['date'].split('-')[1])
        month = int(measurement['date'].split('-')[1])
        total[month-1] += measurement ['value']
print(total)

# Part 2 
# Calculate the sum of the precipitation over the whole year 

total_annual_prec = sum(total)
print(total_annual_prec)

relative_prec = []
for month  in total:
    relative_prec.append(month/total_annual_prec)
    
print(relative_prec)