import json
from random import choice
def gen_person():
    name=''
    tel=''
    letters=['a','b','c','d','e','f','g','v','i','k']
    nums=['1','2','3','4','5','6','7']
    while len(name)!=3:
        name+=choice(letters)
    print(name.capitalize())
    while len(tel)!=5:
            tel+=choice(nums)
    person=input('Ievadiet lietotāja vārdu:')
    return person
    #print('2'+ tel)
def main():
    person=[]
    for i in range(5):
        person.append(gen_person())
    with open('person.json','w') as file:
         json.dump(person, file, indent=2, ensure_ascii=False)
    print(person)
main()