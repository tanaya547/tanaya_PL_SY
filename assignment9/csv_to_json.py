import csv
import json

with open("sample.csv", "r") as csv_file:
    csv_data = csv.DictReader(csv_file)
    data = list(csv_data)

with open("sample.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data converted to JSON successfully!")
