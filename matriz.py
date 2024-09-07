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

def leerMatriz(tipo):
    a = []
    m = 0
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
                input("El valor ingresado debe ser un numero entero. Presione ENTER para continuar.")
                pase = False
                continue
            if m <= 1 or n <= 1:
                input("Los enteros ingresados deben ser positivos mayores a 1. Presione ENTER para continuar.")
                pase = False

    if tipo == "c":
        for i in range(m):
            a.append([])
            for j in range(m + 1):
                if j < m:
                    f = validarCoeficiente(f"Inserte el coeficiente en la posicion [{i}][{j}]: ")
                else:
                    f = validarCoeficiente(f"Inserte el valor de la columna aumentada para la fila [{i}]: ")
                a[i].append(f)
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

def mostrarMatriz(matriz):
    ancho = 10
    
    for fila in matriz:
        print("(", end=" ")
        print("  ".join(f"{str(fila[i]):>{ancho}}" for i in range(len(fila) - 1)), end="  |")
        print("  ".join(f"{str(fila[len(fila) - 1]):>{ancho}}"), end=" )\n")
    print()

def mostrarSistema(matriz):
    print("Solucion del sistema")
    for fila in matriz:
        print("{", end="")
        for i in range(len(fila)):
            if i < len(fila) - 1:
                if fila[i] == 1:
                    print(f"  x{i + 1}", end="")
                else:
                    print("    ", end="")
            else:
                print(f" = {fila[i]}")
