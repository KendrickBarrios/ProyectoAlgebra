import copy
from fractions import Fraction
import matriz
import eliminacionGaussiana as gauss
import escalon
import vector
import operacionesVectores
import operacionesMatrices
import det
import cramer
import inversa
import funciones
import biseccion
from sympy import symbols, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import os

def main():
    op = "."
    while op != "14":
        os.system("cls")
        print("Proyecto de Algebra Lineal\n")
        print("Opciones")
        print("1. Reducir mediante Eliminacion Gaussiana")
        print("2. Reducir a Forma escalonada")
        print("3. Sumar vectores")
        print("4. Multiplicar vectores")
        print("5. Transponer matriz")
        print("6. Producto de matriz por una suma de vectores")
        print("7. Suma de matrices")
        print("8. Producto de matrices/vectores")
        print("9. Calcular el determinante de una matriz")
        print("10. Aplicar regla de Cramer")
        print("11. Obtener la inversa de una matriz")
        print("12. Encontrar raiz de una funcion por metodo de biseccion")
        print("14. Salir del programa\n")
        op = input("Elija la opcion que desea realizar: ")
        print("")

        if op == "1":
            m = matriz.leerMatriz("c")
            os.system("cls")
            print("1. Eliminacion Gaussiana\n")
            print("Matriz original")
            matriz.mostrarMatriz(m)
            s = gauss.resolverMatriz(m)
            if s is not None:
                matriz.mostrarUnicaGauss(m)
            input("\nPresione ENTER para continuar.")
        elif op == "2":
            os.system("cls")
            print("2. Forma escalonada\n")
            m = matriz.leerMatriz("r")
            os.system("cls")
            print("Matriz original")
            matriz.mostrarMatriz(m)
            escalon.formaEscalonada(m)
            input("\nPresione ENTER para continuar.")
        elif op == "3":
            os.system("cls")
            titulo = "3. Sumar vectores\n"
            print(titulo)
            _, _, _, resultado = operacionesVectores.sumaVectores(titulo)
            vector.mostrarResultadoSumaVectores(resultado)
            input("\nPresione ENTER para continuar.")
        elif op == "4":
            os.system("cls")
            titulo = "4. Multiplicar vectores\n"
            print(titulo)
            operacionesVectores.multVectores(titulo)
            input("\nPresione ENTER para continuar.")
        elif op == "5":
            os.system("cls")
            titulo = "5. Transponer matriz\n"
            print(titulo)
            a, b = matriz.generarTranspuesta()
            matriz.mostrarTranspuesta(titulo, a, b)
            input("\nPresione ENTER para continuar.")
        elif op == "6":
            os.system("cls")
            titulo = "6. Producto de matriz por una suma de vectores\n"
            print(titulo)
            resultado, proceso1, proceso2, proceso3, _, _ = operacionesVectores.productoMatrizSuma(titulo)
            os.system("cls")
            print(titulo)
            print("Suma de vectores\n")
            vector.mostrarResultado(resultado)
            print("\nMatriz por suma de vectores\n")
            vector.mostrarResultado(proceso1)
            print("")
            print("\nMatriz por cada vector\n")
            for i in range(len(proceso2)):
                vector.mostrarResultado(proceso2[i])
                print("")
            print("Suma de productos individuales\n")
            vector.mostrarResultado(proceso3)
            input("\nPresione ENTER para continuar.")
        elif op == "7":
            os.system("cls")
            titulo = "7. Suma de matrices\n"
            matrices, escalares, resultado = operacionesMatrices.sumaMatrices("6. Suma de matrices\n")
            print("\n" + titulo + "\n")
            operacionesMatrices.mostrarSumaMatrices(matrices, escalares, resultado)
            input("\nPresione ENTER para continuar.")
        elif op == "8":
            os.system("cls")
            titulo = "8. Producto de matrices/vectores\n"
            operacionesMatrices.productoMatrices(titulo)
            input("\nPresione ENTER para continuar.")
        elif op == "9":
            mat = matriz.leerMatriz("cs")
            procedimiento, matrices, determinante = det.calcularDeterminante(mat)
            os.system("cls")
            print("9. Calcular el determinante de una matriz\n")
            det.mostrarResultado(mat, procedimiento, matrices)
            print(f"\nEl determinante de la matriz ingresada es: {determinante}")
            input("\nPresione ENTER para continuar.")
        elif op == "10":
            mat = matriz.leerMatriz("c")
            mensaje, matrices, determinante, matC, b, matAib, pasosMatAib, mensajesMatAib, determinantesAib, solucion = cramer.aplicarCramer(copy.deepcopy(mat))
            titulo = "10. Aplicar regla de Cramer\n"
            os.system("cls")
            print(titulo)
            if determinante == 0:
                det.mostrarResultado(mat, mensaje, matrices)
                print("\nDado que el determinante es 0, la matriz no puede ser resuelta con el método de Cramer.\n")
                resolver = input("Ingrese 'Y' para resolver la matriz por forma escalonada, o cualquier otro valor para continuar: ").capitalize()
                if resolver == "Y":
                    os.system("cls")
                    print("Matriz original")
                    matriz.mostrarMatriz(mat)
                    escalon.formaEscalonada(mat)
            else:
                det.mostrarResultado(mat, mensaje, matrices)
                print(f"\nDeterminante de la matriz original: {determinante}")
                print("\nMatriz sin columna aumentada")
                matriz.mostrarMatrizS(matC)
                print("\nColumna aumentada")
                matriz.mostrarMatrizS(b)
                for i in range(len(matAib)):
                    print(f"Matriz A{i+1}(b)")
                    det.mostrarResultado(matAib[i], mensajesMatAib[i], pasosMatAib[i])
                    print(f"Determinante de la matriz A{i+1}(b) = {determinantesAib[i]}\n")
                print("Solucion del sistema")
                cramer.mostrarSolucionCramer(determinante, determinantesAib, solucion)
            input("\nPresione ENTER para continuar.")
        elif op == "11":
            mat = matriz.leerMatriz("cs")
            os.system("cls")
            procedimiento, matrices, determinante = det.calcularDeterminante(copy.deepcopy(mat))
            if determinante == 0:
                det.mostrarResultado(mat, procedimiento, matrices)
                print("\nDado que la matriz es singular, no tiene inversa.")
            else:
                inv = inversa.generarIdentidad(mat)
                print("Matriz [ A  I ]")
                matriz.mostrarMatrizInvertible(mat, inv)
                inv = inversa.calcularInversa(mat, inv)
                print("\nMatriz inversa:")
                matriz.mostrarMatrizS(inv)
            input("\nPresione ENTER para continuar.")
        elif op == "12":
            titulo = "12. Encontrar raiz de una funcion por metodo de biseccion\n"
            os.system("cls")
            print(titulo)
            funcion = funciones.leerFuncion()
            print("")
            intervalo = funciones.leerIntervalo()
            multi = input("\nDesea encontrar todas las raices existentes en el intervalo? (s/n): ").lower()
            os.system("cls")
            if multi == "s":
                raiz, mensaje = biseccion.metodoBiseccionMultiraiz(funcion, intervalo)
            else:
                raiz, mensaje = biseccion.metodoBiseccion(funcion, intervalo)
            print(titulo)
            vector.mostrarResultado(mensaje)
            input("\nPresione ENTER para continuar.")
        elif op == "14":
            os.system("cls")
            print("Gracias por usar el programa.")
            input("Presione ENTER para continuar.")
        else:
            print("Por favor elija una opcion valida. (1-2).")
            input("Presione ENTER para continuar.")

if __name__ == "__main__":
    main()