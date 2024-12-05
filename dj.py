import json
country=input('Ievadiet valsts apzīmējumu:')
capital=input('Ievadiet valsts galvaspilsētu:')
new_data={'country':country, 'capital': capital}
data=[]
data.append(new_data)
with open('country.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data,indent=4, ensure_ascii=False))
print('Dati ir veiksmīgi saglabāti!')