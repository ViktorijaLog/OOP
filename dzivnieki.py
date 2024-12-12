import json
def create_json():
    json_data=[{"name": "Tom", "age":"9", "breed":"Haski"}]
    with open('dzivnieks.json','w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
def add_to_json():
    name= input ("Vārds:")
    age=input("Vecums:")
    breed=input("Suga:")
    json_data={"name": name, "age": age, "breed": breed,}
    try:
        data=json.load(open('dzivnieks.json'))
    except:
        data=[]
    data.append(json_data)
def read_and_print_json():
        with open("data.json","r", encoding="utf-8") as f:
           data=json.load(f)
           print("\nPašreizējie dati JSON failā:")
           for record in data:
             print(f"Vārds: {record['name']}, Vecums: {record['age']}, Suga: {record['breed']} ")
while True:
    print('Ievadiet 1-izveidot json failu no jauna, 2-pievienot datus, 3- exit:')
    ievade=int(input('Ievadiet numuru:'))
    if ievade==1:
        create_json()
    elif ievade==2:
       add_to_json()
    else:
        break
#add_to_json()