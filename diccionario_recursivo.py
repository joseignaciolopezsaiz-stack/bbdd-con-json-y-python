import json
with open("diccionario_libros.json", 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)



#datos = {"contador":  0}
print(datos["contador"])
repetir = True
contador = datos["contador"]
while repetir:
    si = input("nuevo elemento ¿si-no? > ")
    if si == "si":
        contador +=1
        datos["contador"] = contador
        codigo = "COD" + str(contador)
        print(codigo)
        datos[codigo] = {"titulo": input("titulo "),
        "autor": input("autor "),
        "cantidad": int(input("cantidad "))
        
        
        }
    else:
        repetir = False
print(datos)

with open("diccionario_libros.json", 'w', encoding='utf-8') as archivo:
    archivo = json.dump(datos)

        