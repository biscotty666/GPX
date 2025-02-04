'''
Convert a directory of gpx files to csv.

The script captures trek points with coordinates,
elevation and time stamp as trek name and weather conditions.

The script requires an input directory.

'''
from bs4 import BeautifulSoup
import csv
import sys
import pathlib
import os

if len(sys.argv) < 2:
    sys.exit("Must supply an input directory")
inPath = sys.argv[1]

def getFiles(inPath):
    return [os.path.join(inPath, f) for f in os.listdir(inPath) if f.endswith(".gpx")]

files = getFiles(inPath)
cfile = str(os.path.join(inPath, 'combined.csv'))
print(cfile, type(cfile))
with open(cfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'Name', 'Lat', 'Lon', 'Elev', 'Time',
                        'Temp', 'Weather', 'Sport'])

for gpx_file in files:
    with open(gpx_file, 'r') as f:
       contents = f.read()

    soup = BeautifulSoup(contents, 'xml')

    tracks = soup.find_all('trkpt')
    elevations = soup.find_all('ele')
    times = soup.find_all('time')
    temp = soup.find('s2t:temperature').text
    weather = soup.find('s2t:weather').text
    sport = soup.find('s2t:sport').text
    name = soup.find('name').text
    sf_name =  os.path.splitext(gpx_file)[0]
    id = os.path.split(sf_name)[1]
    csv_file = sf_name + '.csv'
    data = []

    for track, elevation, time in zip(tracks, elevations, times):
        latitude = track['lat']
        longitude = track['lon']
        elevation_value = elevation.text
        time = time.text
        data.append([id, name, latitude, longitude, elevation_value,
                    time, temp, weather, sport])

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Id', 'Name', 'Lat', 'Lon', 'Elev', 'Time',
                        'Temp', 'Weather', 'Sport'])
        writer.writerows(data)

    with open(cfile, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
