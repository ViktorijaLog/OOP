import json
from pprint import pprint
from random import randint as rd, choice as ch
def write(data,filename):
    data=json.dumps(data)
    data=json.loads(str(data))
    with open(filename,"w",encoding="utf-8" ) as file:
        json.dump(data, file, indent=4)
def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
class User:
    def __init__(self):
       self.name=ch(['First', 'Second', 'Third'])
       self.age=rd(0,100)
       self.id=rd(0,100)
data={
    "user": []
}
for i in range(100):
    data['user'].append(User().__dict__)
write(data, 'data.json')
#input(data)
#pprint(read('data.json'))
n_data=read('data.json')
print(n_data["user"][0])