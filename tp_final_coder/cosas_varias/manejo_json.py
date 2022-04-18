import json

text = '[{"model": "comida.comida", "pk": 1, "fields": {"id_comida": 1, "nombre": "Asado"}}, {"model": "comida.comida", "pk": 3, "fields": {"id_comida": 2, "nombre": "Arroz blanco"}}, {"model": "comida.comida", "pk": 4, "fields": {"id_comida": 3, "nombre": "Arroz integral"}}, {"model": "comida.comida", "pk": 5, "fields": {"id_comida": 2, "nombre": "Lentejas"}}, {"model": "comida.comida", "pk": 6, "fields": {"id_comida": 123123, "nombre": "Garbanzos"}}]'


jtext = json.loads(text)

tupla_comida = []

res_opc = int(input('Igresar opcion... '))

for item in jtext:
    item_comida = (item["pk"],item["fields"]["nombre"])
    tupla_comida.append(item_comida)

for item in tupla_comida:
    if item[0] == res_opc:
        print(item[1])
