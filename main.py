from fractions import Fraction
import matriz
import eliminacionGaussiana as gauss
import escalon
import operacionesVectores
import os

def main():
    op = "."
    while op != "5":
        os.system("cls")
        print("Proyecto de Algebra Lineal\n")
        print("Opciones")
        print("1. Reducir mediante Eliminacion Gaussiana")
        print("2. Reducir a Forma escalonada")
        print("3. Sumar vectores")
        print("4. Multiplicar vectores")
        print("5. Salir del programa\n")
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
                matriz.mostrarSistema(m)
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
            print("3. Sumar vectores\n")
            operacionesVectores.sumaVectores()
            input("\nPresione ENTER para continuar.")
        elif op == "4":
            os.system("cls")
            print("4. Multiplicar vectores\n")
            operacionesVectores.multVectores()
            input("\nPresione ENTER para continuar.")
        elif op == "5":
            print("Gracias por usar el programa.")
            input("Presione ENTER para continuar.")
        else:
            print("Por favor elija una opcion valida. (1-2).")
            input("Presione ENTER para continuar.")

if __name__ == "__main__":
    main()