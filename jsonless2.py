import json
with open('sample2.json', 'r', encoding='UTF8') as file:
    data = json.load(file)
    print(data)

for person in data['people']:
    if person['has_licence'] == False:
        del person['has_licence']

print(data)

with open('sample_edited.json', 'w') as file:
    json.dump(data, file, indent=2)
