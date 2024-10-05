# Abrir el archivo parroquias_Cayambe.txt en modo lectura
file = open('parroquias_Cayambe.txt', 'r')

# Leer y mostrar cada línea del archivo
line = file.readline()
while line:
    print(line.strip())  # Mostrar la línea eliminando el salto de línea al final
    line = file.readline()

# Cerrar el archivo
file.close()