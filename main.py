from fractions import Fraction
import matriz
import eliminacionGaussiana as gauss
import escalon
import vector
import operacionesVectores
import operacionesMatrices
import os

def main():
    op = "."
    while op != "9":
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
        print("9. Salir del programa\n")
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
            sel = input("1. Resolver matriz ejemplo\n2. Leer una nueva matriz\n\nElija:")
            if sel == "1":
                m = [[Fraction(2), Fraction(0), Fraction(1), Fraction(3)], [Fraction(1), Fraction(-1), Fraction(-1), Fraction(1)], [Fraction(3), Fraction(-1), Fraction(0), Fraction(4)]]
                matriz.mostrarMatriz(m)
                escalon.formaEscalonada(m)
            elif sel == "2":
                m = matriz.leerMatriz("r")
                os.system("cls")
                print("Matriz original")
                matriz.mostrarMatriz(m)
                escalon.formaEscalonada(m)
            else:
                print("Opcion no valida.")
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
            print("Gracias por usar el programa.")
            input("Presione ENTER para continuar.")
        else:
            print("Por favor elija una opcion valida. (1-2).")
            input("Presione ENTER para continuar.")

if __name__ == "__main__":
    main()