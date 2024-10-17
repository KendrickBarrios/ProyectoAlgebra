import copy
import matriz
from fractions import Fraction

def calcularDeterminante(mat):
    mensaje = []
    matrices = []
    intercambios = 0
    det = 1  # Para calcular el determinante
    n = len(mat)
    m = len(mat[0])

    columnaCero = False
    for i in range(m):
        columnaCero = True
        for j in range(n):
            if mat[j][i] != 0:
                columnaCero = False
                break
        if columnaCero:
            mensaje.append(f"Dado que todas las entradas de la columna [{i}], la matriz es linealmente dependiente.\n")
            return mensaje, 0  # El determinante es 0

    # Proceso de eliminación de Gauss para obtener la matriz triangular superior
    for i in range(min(n, m)):
        # Si el elemento diagonal es 0, buscamos una fila para intercambiar
        if mat[i][i] == 0:
            for j in range(i + 1, n):
                if mat[j][i] != 0:
                    mat[i], mat[j] = mat[j], mat[i]
                    intercambios += 1
                    mensaje.append(f"f{i + 1} <-> f{j + 1}\n")
                    matrices.append(copy.deepcopy(mat))
                    break

        # Si todavía es 0 después de intentar el intercambio, la matriz es singular
        if mat[i][i] == 0:
            mensaje.append(f"La matriz es singular, determinante es 0.\n")
            return mensaje, 0
        
        # Hacemos ceros debajo del pivote
        for j in range(i + 1, n):
            if mat[j][i] != 0:
                factor = mat[j][i] / mat[i][i]
                for k in range(i, m):
                    mat[j][k] -= factor * mat[i][k]
                mensaje.append(f"f{j + 1} -> f{j + 1} - ({factor})f{i + 1}\n")
                matrices.append(copy.deepcopy(mat))

    # Cálculo del determinante
    for i in range(min(n, m)):
        det *= mat[i][i]

    # Ajustar el signo del determinante según los intercambios
    if intercambios % 2 != 0:
        det *= -1

    return mensaje, matrices, det

def mostrarResultado(mat, mensaje, matrices):
    matriz.mostrarMatrizS(mat)
    print("")
    for i in range(len(matrices)):
        print(mensaje[i])
        matriz.mostrarMatrizS(matrices[i])