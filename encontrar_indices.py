def encontrar_indices(X, Y, Z):
    n, m = len(X), len(Y)

    # Si las longitudes no coinciden, no es posible formar Z
    if len(Z) != n + m:
        return None, None

    # Crear la tabla dp con dimensiones (n+1) x (m+1)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Caso base: una cadena vacía intercalada con otra vacía da una vacía
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

    # Si no es posible formar Z, devolver None
    if not dp[n][m]:
        return None, None

    # Reconstruir las secuencias de índices X' y Y'
    i, j = n, m
    X_indices = []
    Y_indices = []

    # Recorrer hacia atrás desde dp[n][m] para encontrar el camino
    while i > 0 or j > 0:
        if i > 0 and dp[i - 1][j] and X[i - 1] == Z[i + j - 1]:
            X_indices.append(i + j)  # Añadir el índice en Z
            i -= 1
        elif j > 0 and dp[i][j - 1] and Y[j - 1] == Z[i + j - 1]:
            Y_indices.append(i + j)  # Añadir el índice en Z
            j -= 1

    # Los índices fueron agregados en orden inverso, así que revertirlos
    X_indices.reverse()
    Y_indices.reverse()

    return X_indices, Y_indices

# Ejemplo de uso
X = ['C', 'A', 'S', 'A']
Y = ['C', 'A', 'R', 'R', 'O']
Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']

X_indices, Y_indices = encontrar_indices(X, Y, Z)
print("Índices de X' en Z:", X_indices)
print("Índices de Y' en Z:", Y_indices)

import unittest

#Pruebas unitarias
class TestEncontrarIndices(unittest.TestCase):
    def test_example_case(self):
        X = ['C', 'A', 'S', 'A']
        Y = ['C', 'A', 'R', 'R', 'O']
        Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertEqual(X_indices, [2, 3, 4, 9])
        self.assertEqual(Y_indices, [1, 5, 6, 7, 8])

    def test_invalid_case(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'D', 'B', 'E']  # No es posible con un extra 'E'
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertIsNone(X_indices)
        self.assertIsNone(Y_indices)

    def test_exact_match(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'B', 'D']  # Coincide perfectamente
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertEqual(X_indices, [0, 2])
        self.assertEqual(Y_indices, [1, 3])

    def test_empty_sequences(self):
        X = []
        Y = []
        Z = []
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertEqual(X_indices, [])
        self.assertEqual(Y_indices, [])

    def test_one_empty_sequence(self):
        X = ['A', 'B']
        Y = []
        Z = ['A', 'B']  # Barajado posible con Y vacía
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertEqual(X_indices, [0, 1])
        self.assertEqual(Y_indices, [])

    def test_no_possible_interleave(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'B', 'C', 'C']  # No se puede intercalar, un extra 'C'
        X_indices, Y_indices = encontrar_indices(X, Y, Z)
        self.assertIsNone(X_indices)
        self.assertIsNone(Y_indices)

if __name__ == '__main__':
    unittest.main()