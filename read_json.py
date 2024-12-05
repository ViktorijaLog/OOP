import json
with open('country.json','r', encoding='utf-8') as f:
    #data=json.load(f)
    data=json.loads(f.read())
    print(data)