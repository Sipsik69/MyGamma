
import json

json_string = '''
{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true
    }
  ]
}'''

data = json.loads(json_string)
# print(type(data))
print(data)
# print(type(data['people']))
# print(data['people'])
# for person in data['people']:
#     print(person)
#     print('mail: ',person['emails'])
#
# people = data['people'][1]
# print(people['name'], people['phone'])
#
# for person in data['people']:
#     del person['phone']
#     print(person)
#     print(type(person))

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)
people = data['people']
person= people[0]
print(person['name'])
print(person['emails'])
print(person['phone'])