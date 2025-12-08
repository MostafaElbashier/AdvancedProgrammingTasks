import json 
def csv_to_json(csv_file, json_file): 
data = {"people": []} 
with open(csv_file, 'r') as f: 
reader = csv.DictReader(f) 
for row in reader: 
row["Age"] = int(row["Age"]) 
data["people"].append(row) 
with open(json_file, 'w') as f: 
json.dump(data, f)
