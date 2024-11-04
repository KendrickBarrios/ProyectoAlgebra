from fractions import Fraction
import os

def validarCoeficiente(mensaje):
    pase = False
    while not pase:
        c = input(mensaje)
        pase = True
        try:
            if c.find("/") > -1:
                num = int(c[:c.find("/")])
                dem = int(c[c.find("/") + 1:])
                f = Fraction(num, dem)
            else:
                f = Fraction(float(c))
        except ValueError:
            pase = False
            input("El valor ingresado no es valido. Presione ENTER para continuar.")
    return f

# c: Cuadrada
# r: Rectangular
# s: Sin columna aumentada
def leerMatriz(tipo):
    a = []
    m = 0
    n = 0
    pase = False
    while not pase:
        os.system("cls")
        print("Lectura de matriz")
        pase = True
        if tipo == "c":
            try:
                m = int(input("Ingrese el numero de filas y columnas que tendra la matriz (sin contar la columna aumentada): "))
            except ValueError:
                input("El valor ingresado debe ser un numero entero. Presione ENTER para continuar.")
                pase = False
                continue
            if m <= 1:
                input("El entero ingresado debe ser positivo mayor a 1. Presione ENTER para continuar.")
                pase = False
        elif tipo == "r":
            try:
                m = int(input("Ingrese el numero de filas que tendra la matriz: "))
                n = int(input("Ingrese el numero de columnas que tendra la matriz (sin contar la columna aumentada): "))
            except ValueError:
                input("Los valores ingresados deben ser numeros enteros. Presione ENTER para continuar.")
                pase = False
                continue
            if m <= 1 or n <= 1:
                input("Los enteros ingresados deben ser positivos mayores a 1. Presione ENTER para continuar.")
                pase = False
        elif tipo == "s":
            try:
                m = int(input("Ingrese el numero de filas que tendra la matriz: "))
                n = int(input("Ingrese el numero de columnas que tendra la matriz: "))
            except ValueError:
                input("Los valores ingresados deben ser numeros enteros. Presione ENTER para continuar.")
                pase = False
                continue
            if m <= 0 or n <= 0:
                input("Los enteros ingresados deben ser mayores a 0. Presione ENTER para continuar.")
                pase = False
        elif tipo == "cs":
            try:
                m = int(input("Ingrese el numero de filas y columnas que tendra la matriz: "))
            except ValueError:
                input("El valor ingresado debe ser un numero entero. Presione ENTER para continuar.")
                pase = False
            if m <= 1:
                input("El entero ingresado debe ser positivo mayor a 1. Presione ENTER para continuar.")
                pase = False
        elif tipo == "xs":
            try:
                m = int(input("Ingrese el numero de filas que tendran las matrices: "))
                n = int(input("Ingrese el numero de columnas que tendran las matrices: "))
                x = int(input("Ingrese la cantidad de matrices a leer: "))
            except ValueError:
                input("Los valores ingresados deben ser numeros enteros. Presione ENTER para continuar.")
                pase = False
                continue
            if m <= 1 or n <= 1:
                input("Los enteros ingresados deben ser positivos mayores a 1. Presione ENTER para continuar.")
                pase = False



    print()
    if tipo == "c":
        for i in range(m):
            a.append([])
            for j in range(m + 1):
                if j < m:
                    f = validarCoeficiente(f"Inserte el coeficiente en la posicion [{i}][{j}]: ")
                else:
                    f = validarCoeficiente(f"Inserte el valor de la columna aumentada para la fila [{i}]: ")
                a[i].append(f)
        return a
    elif tipo == "r":
        for i in range(m):
            a.append([])
            for j in range(n + 1):
                if j < n:
                    f = validarCoeficiente(f"Inserte el coeficiente en la posicion [{i}][{j}]: ")
                else:
                    f = validarCoeficiente(f"Inserte el valor de la columna aumentada para la fila [{i}]: ")
                a[i].append(f)
        return a
    elif tipo == "s" or tipo == "cs":
        if tipo == "cs":
            n = m
        for i in range(m):
            a.append([])
            for j in range(n):
                f = validarCoeficiente(f"Inserte el coeficiente en la posicion [{i}][{j}]: ")
                a[i].append(f)
        return a
    elif tipo == "xs":
        matrices = []
        escalares = []
        for i in range(x):
            matrices.append([])
            escalares.append(validarCoeficiente(f"\nInserte el escalar por el que se multiplicara la matriz [{i}]: "))
            print(f"\nMatriz {i}")
            for j in range(m):
                matrices[i].append([])
                for k in range(n):
                    matrices[i][j].append(validarCoeficiente(f"Inserte el coeficiente en la posicion [{j}][{k}]: "))
        return matrices, escalares


# mostrar matriz con columna aumentada
def mostrarMatriz(matriz):
    ancho = 10
    
    for fila in matriz:
        print("[", end=" ")
        print("  ".join(f"{str(fila[i]):>{ancho}}" for i in range(len(fila) - 1)), end="        |")
        print("  ".join(f"{str(fila[len(fila) - 1]):>{ancho}}"), end=" ]\n")
    print()

# mostrar matriz sin columna aumentada
def mostrarMatrizS(matriz):
    ancho = 10
    
    for fila in matriz:
        print("[", end=" ")
        print("  ".join(f"{str(fila[i]):>{ancho}}" for i in range(len(fila))), end="        ]\n")
    print()

def mostrarMatrizInvertible(matriz, inversa):
    ancho = 10
    
    for i in range(len(matriz)):
        print("[", end=" ")
        # for j in range(len(matriz[0])):
        #     for k in range(2):
        #         if k == 0:
        #             print(f"{str(matriz[i][j]):^ancho}")
        #             else
        for k in range(2):
            for j in range(len(matriz[0])):
                if k == 0:
                    print(f"{str(matriz[i][j]):^{ancho}}", end="")
                else:
                    print(f"{str(inversa[i][j]):^{ancho}}", end="")
            if k == 0:
                print(" |", end=" ")
            else:
                print("]")

    print()

def mostrarUnicaGauss(matriz):
    print("Solucion del sistema\n")
    for fila in matriz:
        print("{", end="")
        for i in range(len(fila)):
            if i < len(fila):
                if fila[i] == 1:
                    print(f"  x{i + 1}", end="")
                else:
                    print("    ", end="")
        print(f" = {fila[i]}")

def mostrarInconsistente(matriz):
    print("El sistema no tiene solucion\n")
    mostrarMatriz(matriz)

def mostrarInfinitas(matriz):
    print("El sistema tiene infinitas soluciones\n")
    filas = len(matriz)
    columnas = len(matriz[0])
    
    noLibres = []
    mensajes = {}

    for i in range(filas):
        for k in range(columnas - 1):
            mensaje = ""
            if matriz[i][k] != 0 and k not in noLibres:
                noLibres.append(k)
                mensaje += "{ " + f"x{k + 1} ="
                if matriz[i][columnas - 1] != 0:
                    mensaje += f" {matriz[i][columnas - 1]} "
                for l in range(k + 1, columnas - 1):
                    if matriz[i][l] < 0:
                        if mensaje[len(mensaje) - 1] == "=":
                            mensaje += f" {abs(matriz[i][l])}x{l + 1}"
                        else:
                            mensaje += f" + {abs(matriz[i][l])}x{l + 1}"
                    elif matriz[i][l] > 0:
                        mensaje += f" - {matriz[i][l]}x{l + 1}"
                mensajes[k] = mensaje
                break

    for i in range(columnas - 1):
        if i in noLibres:
            print(mensajes[i])
        else:
            print("{ " + f"x{i + 1} es libre")
            
def transponer(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_to_str(matrix):
    return [[str(element) for element in row] for row in matrix]

def mostrarFactores(a, b, t1, t2, o):
    if o:
        m1 = "A"
        m2 = "B"
    else:
        m1 = "B"
        m2 = "A"

    if t1:
        m1 += "t"

    if t2:
        m2 += "t"

    # Imprimir la matriz a o su transpuesta
    print(f"\n{m1}:")
    if t1:
        a_transpuesta = transponer(a)
        a_t_str = matrix_to_str(a_transpuesta)
        for row in a_t_str:
            print(row)
    else:
        a_str = matrix_to_str(a)
        for row in a_str:
            print(row)

    print(f"\n{m2}:")
    # Imprimir la matriz b o su transpuesta
    if t2:
        b_transpuesta = transponer(b)
        b_t_str = matrix_to_str(b_transpuesta)
        for row in b_t_str:
            print(row)
    else:
        b_str = matrix_to_str(b)
        for row in b_str:
            print(row)

def generarTranspuesta():
    a = leerMatriz("s")
    b = transponer(a)
    return a, b

def mostrarTranspuesta(titulo, a, b):
    print(titulo)
    print("Matriz original: ")
    mostrarMatrizS(a)
    print("\nMatriz transpuesta: ")
    mostrarMatrizS(b)