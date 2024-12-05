import json
from random import choice
def gen_person():
    name=input('Ievadiet lietotāja vārdu:')
    parole=''
    nums=['1','2','3','4','5','6','7']
    while len(nums)!=5:
            parole+=choice(parole)
    person={"name":name.capitalize(), "parole":parole}
    print(name,parole)
def main():
    person=[]
    for i in range(5):
        person.append(gen_person())
    with open('person.json','w') as file:
         json.dump(person, file, indent=2, ensure_ascii=False)
    print(person)
main()