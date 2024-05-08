import json

with open("secret.json") as f:
    json_file = f.read()
    key = json.loads(json_file)
    print(key)