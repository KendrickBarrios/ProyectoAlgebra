import matriz
import fractions
import os

def leerVector(mensaje):
    v = []
    n = 0
    pase = False
    while not pase:
        os.system("cls")
        pase = True
        try:
            n = int(input("Ingrese el numero de dimensiones que tendra el vector: "))
        except ValueError:
            pase = False
            input("El valor ingresado debe ser un numero entero.")
            continue
        if n <= 0:
            pase = False
            input("El numero de dimensiones del vector debe ser mayor a 0.")

    print(mensaje)
    for i in range(n):
        f = matriz.validarCoeficiente(f"Inserte el valor en la posicion [{i}]: ")
        v.append(f)

    return v