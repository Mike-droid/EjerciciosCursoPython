mi_diccionario = {}
mi_diccionario['proweb'] = 9
mi_diccionario['android dev'] = 9
mi_diccionario['algoritmos'] = 8

#Iterar en llaves

for key in mi_diccionario.keys():
    print(key)


for value in mi_diccionario.values():
    print(value)


for llave,valor in mi_diccionario.items():
    print("Llave: {} , Valor: {}".format(llave,valor))