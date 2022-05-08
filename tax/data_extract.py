import json


final_data = {
    "1": [],
    "2": [],
    "Bagmati": [],
    "Gandaki": [], # 4 in json
    "Lumbini": [], # 5 in json
    "Karnali": [],
    "Sudurpaschim": [],
}

# Removing unnecessary data from json and compiling according to province

with open('./tax/data.json', 'r') as data_file:
    data = json.load(data_file)
    for datum in data:
        prov = datum.pop("Province")
        datum.pop("Code")
        datum.pop("Type")
        if prov == "1":
            final_data["1"].append(datum)
        elif prov == "2":
            final_data["2"].append(datum)
        elif prov == "Bagmati":
            final_data["Bagmati"].append(datum)
        elif prov == "Gandaki":
            final_data["Gandaki"].append(datum)
        elif prov == "5":
            final_data["Lumbini"].append(datum)
        elif prov == "Karnali":
            final_data["Karnali"].append(datum)
        elif prov == "Sudurpaschim":
            final_data["Sudurpaschim"].append(datum)


with open('./tax/data_final.json', 'w') as data_file:
    json.dump(final_data, data_file)


print(final_data['1'][0])
print(type(final_data))
for data in final_data['1']:
    if data['District'] == 'BHOJPUR':
        print(data)

