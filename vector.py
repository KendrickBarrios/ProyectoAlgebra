import matriz
import os

def leerDimensiones(mensaje):
    pase = False
    while not pase:
        pase = True
        try:
            n = int(input(mensaje))
        except ValueError:
            pase = False
            input("El valor ingresado debe ser un numero entero. Presione ENTER para continuar.")
            continue
        if n <= 0:
            pase = False
            input("El numero de dimensiones debe ser mayor a 0. Presione ENTER para continuar.")
    return n

def leerVector(mensaje, n):
    v = []

    print(mensaje)
    for i in range(n):
        f = matriz.validarCoeficiente(f"Inserte el valor en la posicion [{i}]: ")
        v.append(f)

    return v

def mostrarResultado(resultado):
    for fila in resultado:
        print(fila)
