import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

import requests
response = requests.get('http://api.open-notify.org/astros.json')
response_json = json.loads(response.text)
print(response_json)
for item in response_json['people']:
    print(item)

