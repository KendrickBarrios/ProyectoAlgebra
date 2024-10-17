import copy
import matriz
import det
from fractions import Fraction

def aplicarCramer(mat):
    mat2 = copy.deepcopy(mat)
    matC = [] # Matriz sin columna aumentada
    b = [] # Columna aumentada
    matAib = [] # Conjunto de matrices en las que se reemplaza una columna por la aumentada
    pasosMatAib = [] # Procedimiento de obtencion de matrices Ai(b)
    mensajesMatAib = [] # Operaciones para obtener matrices Ai(b)
    determinantesAib = [] # Determinantes de las matrices Ai(b)
    solucion = [] # Solucion del sistema

    # Calculo del determinante de la matriz original
    mensaje, matrices, determinante = det.calcularDeterminante(mat2)
    if determinante == 0:
        return mensaje, matrices, determinante, [None] * 7

    for i in range(len(mat)):
        matC.append([])
        for j in range(len(mat[0])):
            matC[i].append(mat[i][j])


    for i in range(len(mat)):
        b.append([matC[i].pop()])
    

    for i in range(len(mat)):
        matAib.append([])
        pasosMatAib.append([])
        for j in range(len(mat2)):
            matAib[i].append([])
            for k in range(len(matC[0])):
                matAib[i][j].append(matC[j][k])

    for i in range(len(matAib)):
        for j in range(len(matAib[0])):
            matAib[i][j][i] = b[j][0]

    for i in range(len(matAib)):
        mensajeTemp, matricesTemp, determinanteTemp = det.calcularDeterminante(copy.deepcopy(matAib[i])) 
        mensajesMatAib.append(mensajeTemp)
        pasosMatAib.append(matricesTemp)
        determinantesAib.append(determinanteTemp)
        solucion.append(determinantesAib[i]/determinante)

    return mensaje, matrices, determinante, matC, b, matAib, pasosMatAib, mensajesMatAib, determinantesAib, solucion

def mostrarSolucionCramer(determinante, determinantesAib, solucion):
    for i in range(len(solucion)):
        print("x" + f"{i+1} = {determinantesAib[i]}/{determinante} = {solucion[i]}")
    
    print("")
    for i in range(len(solucion)):
        print("{ x" + f"{i+1} = {solucion[i]}")