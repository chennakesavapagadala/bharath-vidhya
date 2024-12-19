import csv
import re
import time
import pandas as pd
from geopy.geocoders import Nominatim

csv_file_path = 'csvfiles/colleges_data.csv'


all_colleges = []
private_colleges = []
government_colleges = []

# Open the CSV file and read the data
def get_coords(location_name):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(location_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return "Location not found"

def csv_file_data():
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for id, row in enumerate(csv_reader):
             # Construct location string using both city and state
            location_name = f"{row['state']}, India"
            # coords = get_coords(location_name)

            all_colleges.append({
                'id'        : id+1,
                'name'      :row['name'],
                'location'  :row['location'],
                'state'     :row['state'],
                # 'coords'    :coords,
                'city'      :row['city'],
                'ranking'   :row['ranking'].strip(),
                'cr360'     :row['ranking'].split('|')[-1].replace('Careers360  Rating: ','').replace('No Ranking','').strip(),
                'nirf'      :row['ranking'].split('|')[0].replace('NIRF Ranking: ','').replace('No Ranking','').strip(),
                'branch'    :row['branch'],
                'exams'     :row['exams'],
                'rating'    :row['rating'],
                'fees'      :row['fees'],
                'type'      :row['type'],
                'links'     :row['links'],
                'gallery'   :row['gallery'],
                'unv_links' :row['unv_links'],
                'unv_gallery':row['unv_gallery']

                })
        for college in all_colleges:
            if 'Private' in college['type']:
                private_colleges.append(college)
            if 'Public/Govt' in college['type']:
                government_colleges.append(college)

csv_file_data()
filter = [college for college in all_colleges if college['nirf'] != '']
def parse_nirf_range(nirf_value):
    if '-' in nirf_value:
        start, end = map(int, nirf_value.split('-'))
        return start  # Use the start of the range for sorting
    return int(nirf_value)
top_colleges = sorted(filter, key=lambda x: parse_nirf_range(x['nirf']))
df = pd.DataFrame(top_colleges)
df.to_csv("csvfiles/top_colleges.csv", index=False)

df = pd.DataFrame(private_colleges)
df.to_csv("csvfiles/private_colleges.csv", index=False)

df = pd.DataFrame(government_colleges)
df.to_csv("csvfiles/government_colleges.csv", index=False)
