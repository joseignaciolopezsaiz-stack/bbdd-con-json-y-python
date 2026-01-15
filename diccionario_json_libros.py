import json

data = {"contador": 0}  # Para un objeto JSON {}
with open("diccionario_libros.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"Archivo creado exitosamente con contenido JSON vacío.")
