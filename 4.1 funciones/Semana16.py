# Abrir el archivo parroquias_Cayambe.txt en modo escritura
file = open('parroquias_Cayambe.txt', 'w')

# Escribir tres parroquias del Canton Cayambe en el archivo
file.write("1. Juan Montalvo\n")
file.write("2. Olmedo\n")
file.write("3. Cangahua\n")

# Cerrar el archivo
file.close()
# Abrir el archivo parroquias_Cayambe.txt en modo lectura
file = open('parroquias_Cayambe.txt', 'r')

# Leer y mostrar cada línea del archivo
line = file.readline()
while line:
    print(line.strip())  # Mostrar la línea eliminando el salto de línea al final
    line = file.readline()

# Cerrar el archivo
file.close()