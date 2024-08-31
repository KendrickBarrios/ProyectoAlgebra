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

def leerMatriz():
    a = []
    m = 0
    pase = False
    while not pase:
        os.system("cls")
        print("Lectura de matriz")
        pase = True
        try:
            m = int(input("Ingrese el numero de filas y de columnas que tendra la matriz (sin contar la columna aumentada): "))
        except ValueError:
            input("El valor ingresado debe ser un numero entero. Presione ENTER para continuar.")
            pase = False
            continue
        if m <= 1:
            input("El entero ingresado debe ser positivo mayor a 1. Presione ENTER para continuar.")
            pase = False


    for i in range(m):
        a.append([])
        for j in range(m + 1):
            if j < m:
                f = validarCoeficiente(f"Inserte el coeficiente en la posicion [{i}][{j}]: ")
                a[i].append(f)

            else:
                f = validarCoeficiente(f"Inserte el valor de la columna aumentada para la fila [{i}]: ")
                a[i].append(f)
    return a
