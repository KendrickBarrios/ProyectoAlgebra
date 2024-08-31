from fractions import Fraction
import matriz
import eliminacionGaussiana as gauss

# Ejemplo de matriz aumentada sin solución
matriz = [
    [Fraction(1), Fraction(-2), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(2), Fraction(-8), Fraction(8)],
    [Fraction(-4), Fraction(5), Fraction(9), Fraction(-9)]
]

print("Matriz original\n")
gauss.mostrarMatriz(matriz)
s = gauss.resolverMatriz(matriz)
gauss.mostrarMatriz(s)