import json

person = {
    'first_name': "John",
    "isAlive": True,
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "hasMortgage": None
}

 
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f,indent=4)
 
 
  
open('person.json', 'r').read()   # reading JSON object as string
'{"hasMortgage": null, "isAlive": true, "age": 27, "address": {"state": "NY", "streetAddress": "21 2nd Street", "city": "New York", "postalCode": "10021-3100"}, "first_name": "John"}'


type(open('person.json', 'r').read())   
