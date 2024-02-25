# mi primer archivo en git
# Archivo: busqueda_matriz.py

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})."
    return f"Valor {valor} no encontrado en la matriz."

# Matriz de ejemplo 3x3
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Llamada a la función y muestra de resultados
resultado_busqueda = buscar_valor(matriz_ejemplo, valor_a_buscar)
print(resultado_busqueda)

# Archivo: ordenacion_matriz.py

def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz

# Matriz de ejemplo 3x3
matriz_ejemplo = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Fila a ordenar
fila_a_ordenar = 1

# Mostrar matriz original
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

# Llamada a la función y muestra de resultados
matriz_ordenada = ordenar_fila(matriz_ejemplo, fila_a_ordenar)
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)