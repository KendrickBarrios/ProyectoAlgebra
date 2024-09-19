import os
import vector
import matriz
import fractions

def sumaVectores():
    v = []
    e = []
    m = 0
    pase = False
    while not pase:
        pase = True
        try:
            m = int(input("Ingrese el numero de vectores a sumar: "))
        except ValueError:
            pase = False
            input("Debe ingresar un numero entero. Presione ENTER para continuar.")
            continue
        if m <= 1:
            pase = False
            input("El numero de vectores a sumar debe ser mayor o igual a 1. Presione ENTER para continuar.")
            
    for i in range(m):
        os.system("cls")
        e.append(matriz.validarCoeficiente(f"Ingrese el escalar por el que se multiplicara el vector {i}: "))
        v.append(vector.leerVector(f"Lectura del vector {i}"))
        if i > 0:
            if len(v[i]) != len(v[0]):
                "No se pueden sumar los vectores, pues no tienen el mismo numero de dimensiones."
                return 
    
    s = []
    resultado = []
    for i in range(len(v[0])):
        suma = 0
        fila = ""

        for j in range(len(v)):
            suma += (e[j] * v[j][i])
            if i != (int(len(v) / 2)):
                fila += " "*8
            else:
                if j == 0:
                    fila += f" {str(e[j]):^6} "
                else:
                    if e[j] >= 0:
                        fila += f"+ {str(e[j]):^6}"
                    else:
                        fila += f"- {str(abs(e[j])):^6}"
            fila += f"[{str(v[j][i]):^10}] "
        if i != (int(len(v) / 2)):
            fila += " "*10 + f"[{str(suma):^10}]"
        else:
            fila += " "*4 + "=" + " "*5 + f"[{str(suma):^10}]"

        resultado.append(fila)
        s.append(suma)

    for fila in resultado:
        print(fila)
