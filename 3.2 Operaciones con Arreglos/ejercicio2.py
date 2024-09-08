# Ejercicio 2 Matriz de 3 x 3
matriz = [
    [15, 1, 9],
    [7, 11, 34],
    [6, 8, 3]
]

print(matriz)

# metodo de ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

print("Matriz original ")
print(matriz)
buble_sort(matriz[1])
print(matriz)

