def validarSecuenciaBottomUp(X, Y, Z):
    n, m = len(X), len(Y)

    # Si las longitudes no coinciden, no es posible formar Z
    if len(Z) != n + m:
        return False

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

    return dp[n][m]

# Ejemplo de uso
X = ['C', 'A', 'S', 'A']
Y = ['C', 'A', 'R', 'R', 'O']
Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']

if validarSecuenciaBottomUp(X, Y, Z):
    print("La secuencia Z se puede formar al barajar X e Y.")
else:
    print("La secuencia Z no se puede formar al barajar X e Y.")

import unittest

#Pruebas unitarias
class TestSecuenceBottomUp(unittest.TestCase):
    def test_example_case(self):
        X = ['C', 'A', 'S', 'A']
        Y = ['C', 'A', 'R', 'R', 'O']
        Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']
        self.assertTrue(validarSecuenciaBottomUp(X, Y, Z))

    def test_invalid_case(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'D', 'B', 'E']
        self.assertFalse(validarSecuenciaBottomUp(X, Y, Z))

    def test_exact_match(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'B', 'D'] 
        self.assertTrue(validarSecuenciaBottomUp(X, Y, Z))

    def test_empty_sequences(self):
        X = []
        Y = []
        Z = []
        self.assertTrue(validarSecuenciaBottomUp(X, Y, Z))

    def test_one_empty_sequence(self):
        X = ['A', 'B']
        Y = []
        Z = ['A', 'B']
        self.assertTrue(validarSecuenciaBottomUp(X, Y, Z))

    def test_no_possible_interleave(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'B', 'C', 'C']
        self.assertFalse(validarSecuenciaBottomUp(X, Y, Z))

if __name__ == '__main__':
    unittest.main()

