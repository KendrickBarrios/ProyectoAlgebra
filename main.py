from fractions import Fraction
import matriz
import eliminacionGaussiana as gauss
import os

def main():
    op = "."
    while op != "2":
        os.system("cls")
        print("Proyecto de Algebra Lineal\n")
        print("Opciones")
        print("1. Resolver sistema mediante eliminacion Gaussiana")
        print("2. Salir del programa\n")
        op = input("Elija la opcion que desea realizar: ")
        print("")

        if op == "1":
            m = matriz.leerMatriz("c")
            os.system("cls")
            print("Matriz original")
            matriz.mostrarMatriz(m)
            s = gauss.resolverMatriz(m)
            if s is not None:
                matriz.mostrarSistema(m)
            input("\nPresione ENTER para continuar.")
        elif op == "2":
            print("Gracias por usar el programa.")
            input("Presione ENTER para continuar.")
        else:
            print("Por favor elija una opcion valida. (1-2).")
            input("Presione ENTER para continuar.")

if __name__ == "__main__":
    main()