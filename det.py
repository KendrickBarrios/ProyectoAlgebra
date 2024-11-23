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
            return mensaje, [], 0  # El determinante es 0

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

        # Hacemos ceros debajo del pivote
        for j in range(i + 1, n):
            if mat[j][i] != 0:
                factor = mat[j][i] / mat[i][i]
                for k in range(i, m):
                    mat[j][k] -= factor * mat[i][k]
                print(f"f{j + 1} -> f{j + 1} - ({factor})f{i + 1}\n")
                print(mat)
                mensaje.append(f"f{j + 1} -> f{j + 1} - ({factor})f{i + 1}\n")
                matrices.append(copy.deepcopy(mat))

    mensaje.append(f"\nNumero de intercambios realizados: {intercambios}")

    # Cálculo del determinante
    mensaje.append("\n|A| = ")
    for i in range(min(n, m)):
        if i == 0:
            mensaje[-1] += f"{str(mat[i][i])} "
        else:
            mensaje[-1] += f"* {str(mat[i][i])} "
        det *= mat[i][i]
    
    mensaje[-1] += f"= {str(det)}"

    # Ajustar el signo del determinante según los intercambios
    if intercambios % 2 != 0:
        det *= -1

    return mensaje, matrices, det

def mostrarResultado(mat, mensaje, matrices):
    matriz.mostrarMatrizS(mat)
    print("")
    for i in range(len(mensaje)):
        print(mensaje[i])
        if i < len(matrices):
            matriz.mostrarMatrizS(matrices[i])