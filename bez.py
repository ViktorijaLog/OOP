import json
def create_json():
    json_data=[{"name": "Toms", "grade":"12.a",}]
    with open('db.json','w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
def add_to_json():
    name= input ("Vārds:")
    grade=input("Klase:")
    json_data={"name": name, "grade": grade,}
    try:
        data=json.load(open('db.json'))
    except:
        data=[]
    data.append(json_data)
    with open('db.json','w') as file:
        json.dump(data, file,indent=2, ensure_ascii=False)
def read_and_print_json():
        with open("data.json","r", encoding="utf-8") as f:
            data=json.load(f)
            print("\nPašreizējie dati JSON failā:")
            for record in data:
                print(f"Vārds: {record['name']}, Klase: {record['grade']}")
while True:
    print('Ievadiet 1-izveidot json failu no jauna, 2-pievienot datus, 3- exit:')
    ievade=int(input('Ievadiet numuru:'))
    if ievade==1:
        create_json()
    elif ievade==2:
        create_json()
    else:
        break
add_to_json()
#create_json()
