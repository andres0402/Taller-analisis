import random
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def validarSecuenciaMemo(X, Y, Z, i=0, j=0, k=0, memo=None):

    
    # Inicializar el diccionario para memoización si es la primera llamada
    if memo is None:
        memo = {}

    # Caso base: si hemos llegado al final de todas las secuencias
    if k == len(Z):
        return i == len(X) and j == len(Y)

    # Comprobar si el subproblema ya ha sido calculado
    if (i, j, k) in memo:
        return memo[(i, j, k)]

    if i < len(X) and X[i] == Z[k]:
        if validarSecuenciaMemo(X, Y, Z, i + 1, j, k + 1, memo):
            memo[(i, j, k)] = True
            return True
        
    if j < len(Y) and Y[j] == Z[k]:
        if validarSecuenciaMemo(X, Y, Z, i, j + 1, k + 1, memo):
            memo[(i, j, k)] = True
            return True

    # Si no se cumple ninguna condición, la secuencia Z no puede ser formada
    memo[(i, j, k)] = False
    return False

def validarSecuenciaBottomUp(X, Y, Z):
    n, m = len(X), len(Y)

    # Si las longitudes no coinciden, no es posible formar Z
    if len(Z) != n + m:
        return False

    # Crear la tabla dp
    dp = [[False] * (m + 1) for _ in range(n + 1)]


    dp[0][0] = True

    # Rellenar la primera columna (usando solo X para formar Z)
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] and X[i - 1] == Z[i - 1]

    # Rellenar la primera fila (usando solo Y para formar Z)
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] and Y[j - 1] == Z[j - 1]

    # Rellenar el resto de la tabla
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Z[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if Y[j - 1] == Z[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]

    return dp[n][m]

def generarSecuencias(size):
    X = random.choices(['A', 'B', 'C', 'D'], k=size)
    Y = random.choices(['A', 'B', 'C', 'D'], k=size)
    Z = X + Y
    random.shuffle(Z)
    return X, Y, Z

if __name__ == '__main__':
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    memoized_times = []
    bottom_up_times = []
    memoized_memories = []
    bottom_up_memories = []

    # Ejecutar pruebas para diferentes tamaños
    for size in sizes:
        X, Y, Z = generarSecuencias(size)

        # Medir tiempo y memoria para el algoritmo memoizado
        start_time = time.time()
        mem_usage = memory_usage((validarSecuenciaMemo, (X, Y, Z)), max_usage=True)
        memoized_times.append(time.time() - start_time)
        memoized_memories.append(mem_usage)  # Almacenar el valor directamente

        # Medir tiempo y memoria para el algoritmo bottom-up
        start_time = time.time()
        mem_usage = memory_usage((validarSecuenciaBottomUp, (X, Y, Z)), max_usage=True)
        bottom_up_times.append(time.time() - start_time)
        bottom_up_memories.append(mem_usage)  # Almacenar el valor directamente

    # Graficar resultados
    plt.figure(figsize=(12, 6))

    # Graficar tiempos de ejecución
    plt.subplot(1, 2, 1)
    plt.plot(sizes, memoized_times, marker='o', label='Memoizado')
    plt.plot(sizes, bottom_up_times, marker='o', label='Bottom-Up')
    plt.title('Tiempo de Ejecución')
    plt.xlabel('Tamaño de Entrada')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()

    # Graficar uso de memoria
    plt.subplot(1, 2, 2)
    plt.plot(sizes, memoized_memories, marker='o', label='Memoizado')
    plt.plot(sizes, bottom_up_memories, marker='o', label='Bottom-Up')
    plt.title('Uso de Memoria')
    plt.xlabel('Tamaño de Entrada')
    plt.ylabel('Memoria (MB)')
    plt.legend()

    plt.tight_layout()
    plt.show()