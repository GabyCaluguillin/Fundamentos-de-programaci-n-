# Crear el diccionario inicial
# Crea un diccionario de persona

informacion_personal = {
    "nombre": "Marcelo",
    "apellido": "Lanchimba",
    "edad": 30,
    "ciudad": "Cayambe",
    "profesion": "Ingeniero"
}
print(informacion_personal)
print(informacion_personal["nombre"])
print(informacion_personal["apellido"])
print(informacion_personal["edad"])
print(informacion_personal["ciudad"])
print(informacion_personal["profesion"])

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Tabacundo"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniero Mecatronico"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999775345"

# Eliminar la clave "edad"
del informacion_personal["edad"]
print(informacion_personal)

# Imprimir el diccionario final
print(informacion_personal)

{'nombre': 'Marcelo',
 'apellido': 'Lanchimba',
 'ciudad': 'Tabacundo',
 'profesion': 'Ingeniero Mecatronico',
 'telefono': '0999775345'}