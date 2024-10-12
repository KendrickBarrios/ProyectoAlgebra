import matriz
import os
from fractions import Fraction

def sumaMatrices(titulo):
    matrices, escalares = matriz.leerMatriz("xs")
    resultado = []

    for i in range(len(matrices[0])):
        resultado.append([])
        for j in range(len(matrices[0][0])):
            resultado[i].append(0)
    
    for i in range(len(matrices)):
        for j in range(len(matrices[0])):
            for k in range(len(matrices[0][0])):
                resultado[j][k] += (escalares[i] * matrices[i][j][k])
    
    return matrices, escalares, resultado

def mostrarSumaMatrices(matrices, escalares, resultado):
    for i, matriz in enumerate(matrices, start=1):
        print(f"Matriz {i} * {escalares[i-1]}:")
        for fila in matriz:
            fila_str = [str(elem * escalares[i-1]) for elem in fila]
            print(f"  [{', '.join(fila_str)}]")  
        print()
    
    print("Resultado:")
    for fila in resultado:
        fila_str = [str(elem) for elem in fila]
        print(f"  [{', '.join(fila_str)}]")

def productoMatrices(titulo):
    print("Lectura de la matriz A\n")
    a = matriz.leerMatriz("s")
    print("\nLectura de la matriz B")
    b = matriz.leerMatriz("s")
    op = "0"
    while op != 9:
        os.system("cls")
        print(titulo)
        print(f"A: {len(a)}x{len(a[0])}")
        print(f"At: {len(a[0])}x{len(a)}")
        print(f"B: {len(b)}x{len(b[0])}")
        print(f"Bt: {len(b[0])}x{len(b)}")
        print("\n1. A * B")
        print("2. A * BT")
        print("3. AT * B")
        print("4. AT * BT")
        print("5. B * A")
        print("6. B * AT")
        print("7. BT * A")
        print("8. BT * AT")
        print("9. Volver al menu principal")
        op = input("\nIndique la opcion que desea realizar: ")
        
        if op == "1":
            if len(a[0]) != len(b):
                print(f"No es posible efectuar el producto. \nColumnas de A: {len(a[0])} \nFilas de B: {len(b)}")
                
            else:
                resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

                for i in range(len(a)):         # Recorre las filas de a
                    for j in range(len(b[0])):   # Recorre las columnas de b
                        for k in range(len(b)):  # Recorre las filas de b
                            resultado[i][j] += a[i][k] * b[k][j]
                matriz.mostrarFactores(a, b, False, False, True)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "2":
            if len(a[0]) != len(b[0]):
                print(f"No es posible efectuar el producto. \nColumnas de A: {len(a[0])} \nFilas de BT: {len(b[0])}")
                
            else:
                resultado = [[0 for _ in range(len(b))] for _ in range(len(a))]

                for i in range(len(a)):             # Recorre las filas de a
                    for j in range(len(b)):         # Recorre las filas de b (transpuestas en columnas)
                        for k in range(len(b[0])):  # Recorre las columnas de b
                            resultado[i][j] += a[i][k] * b[j][k]  # Usa b transpuesta
                matriz.mostrarFactores(a, b, False, True, True)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "3":
            if len(a) != len(b):
                print(f"No es posible efectuar el producto. \nColumnas de AT: {len(a)} \nFilas de B: {len(b)}")
                
            else:
                resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a[0]))]

                for i in range(len(a[0])):      # Recorre las columnas de a (transpuestas en filas)
                    for j in range(len(b[0])):  # Recorre las columnas de b
                        for k in range(len(a)): # Recorre las filas de a
                            resultado[i][j] += a[k][i] * b[k][j]  # Usa a transpuesta
                matriz.mostrarFactores(a, b, True, False, True)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "4":
            if len(a) != len(b[0]):
                print(f"No es posible efectuar el producto. \nColumnas de AT: {len(a)} \nFilas de BT: {len(b[0])}")
                
            else:
                resultado = [[0 for _ in range(len(b))] for _ in range(len(a[0]))]

                for i in range(len(a[0])):      # Recorre las columnas de a (transpuestas en filas)
                    for j in range(len(b)):     # Recorre las filas de b (transpuestas en columnas)
                        for k in range(len(a)): # Recorre las filas de a
                            resultado[i][j] += a[k][i] * b[j][k]  # Usa a^T y b^T
                matriz.mostrarFactores(a, b, True, True, True)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        if op == "5":
            if len(b[0]) != len(a):
                print(f"No es posible efectuar el producto. \nColumnas de B: {len(b[0])} \nFilas de A: {len(a)}")
                
            else:
                resultado = [[0 for _ in range(len(a[0]))] for _ in range(len(b))]

                for i in range(len(b)):         # Recorre las filas de a
                    for j in range(len(a[0])):   # Recorre las columnas de b
                        for k in range(len(a)):  # Recorre las filas de b
                            resultado[i][j] += b[i][k] * a[k][j]
                matriz.mostrarFactores(b, a, False, False, False)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "6":
            if len(b[0]) != len(a[0]):
                print(f"No es posible efectuar el producto. \nColumnas de B: {len(b[0])} \nFilas de AT: {len(a[0])}")
                
            else:
                resultado = [[0 for _ in range(len(a))] for _ in range(len(b))]

                for i in range(len(b)):             # Recorre las filas de a
                    for j in range(len(a)):         # Recorre las filas de b (transpuestas en columnas)
                        for k in range(len(a[0])):  # Recorre las columnas de b
                            resultado[i][j] += b[i][k] * a[j][k]  # Usa b transpuesta
                matriz.mostrarFactores(b, a, False, True, False)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "7":
            if len(b) != len(a):
                print(f"No es posible efectuar el producto. \nColumnas de BT: {len(b)} \nFilas de A: {len(a)}")
                
            else:
                resultado = [[0 for _ in range(len(a[0]))] for _ in range(len(b[0]))]

                for i in range(len(b[0])):      # Recorre las columnas de a (transpuestas en filas)
                    for j in range(len(a[0])):  # Recorre las columnas de b
                        for k in range(len(b)): # Recorre las filas de a
                            resultado[i][j] += b[k][i] * a[k][j]  # Usa a transpuesta
                matriz.mostrarFactores(b, a, True, False, False)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "8":
            if len(b) != len(a[0]):
                print(f"No es posible efectuar el producto. \nColumnas de BT: {len(b)} \nFilas de AT: {len(a[0])}")
               
            else:
                resultado = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]

                for i in range(len(b[0])):      # Recorre las columnas de a (transpuestas en filas)
                    for j in range(len(a)):     # Recorre las filas de b (transpuestas en columnas)
                        for k in range(len(b)): # Recorre las filas de a
                            resultado[i][j] += b[k][i] * a[j][k]  # Usa a^T y b^T
                matriz.mostrarFactores(b, a, True, True, False)
                print("\nResultado:\n")
                matriz.mostrarMatrizS(resultado)
                resultado.clear()
        elif op == "9":
            input("\nVolviendo al menu principal.")
            return
        input("Presione ENTER para continuar.")
