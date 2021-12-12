import json
import pandas as pd
import os
import csv

f = open(os.path.join(os.getcwd(), "data_collection", "json", "flat_json_hiphop_rock_jazz.json"))
print(f)

resultJson = json.load(f)
 
# now we will open a file for writing
data_file = open('data_file.csv', 'w')
# create the csv writer object
csv_writer = csv.writer(data_file)

count = 0
 
for line in resultJson:
    if count == 0:
 
        # Writing headers of CSV file
        header = line.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(line.values())
 
data_file.close()