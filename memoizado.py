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

# Ejemplo de uso
X = ['C', 'A', 'S', 'A']
Y = ['C', 'A', 'R', 'R', 'O']
Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']

if validarSecuenciaMemo(X, Y, Z):
    print("La secuencia Z se puede formar al barajar X e Y.")
else:
    print("La secuencia Z no se puede formar al barajar X e Y.")

import unittest

#Pruebas unitarias
class TestSecuenceMemo(unittest.TestCase):
    def test_example_case(self):
        X = ['C', 'A', 'S', 'A']
        Y = ['C', 'A', 'R', 'R', 'O']
        Z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'O', 'A']
        self.assertTrue(validarSecuenciaMemo(X, Y, Z))

    def test_invalid_case(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'D', 'B', 'E'] 
        self.assertFalse(validarSecuenciaMemo(X, Y, Z))

    def test_exact_match(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'C', 'B', 'D']  
        self.assertTrue(validarSecuenciaMemo(X, Y, Z))

    def test_empty_sequences(self):
        X = []
        Y = []
        Z = []
        self.assertTrue(validarSecuenciaMemo(X, Y, Z)) 

    def test_one_empty_sequence(self):
        X = ['A', 'B']
        Y = []
        Z = ['A', 'B'] 
        self.assertTrue(validarSecuenciaMemo(X, Y, Z))

    def test_no_possible_interleave(self):
        X = ['A', 'B']
        Y = ['C', 'D']
        Z = ['A', 'B', 'C', 'C']
        self.assertFalse(validarSecuenciaMemo(X, Y, Z))

if __name__ == '__main__':
    unittest.main()