from fractions import Fraction

def mostrarMatriz(matriz):
    for fila in matriz:
        print("(", end=" ")
        print("  ".join("   " + str(fila[i]) + "   " for i in range(len(fila) - 1)), end="|")
        print("   " + str(fila[len(fila) - 1]), end="   ")
        print(")")
    print()

def resolverMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        # Se encuentra el pivote y se intercambian las filas si es necesario
        if matriz[i][i] == 0:
            for j in range(i + 1, filas):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    mensaje = f"f{i + 1} <-> f{j + 1}"
                    print(mensaje)
                    print("-"*(len(mensaje) - 1), end=">\n")
                    print("")
                    mostrarMatriz(matriz)
                    break
            else:
                continue  # Si no encuentra un pivote valido, pasa a la siguiente columna
        
        # Se convierte el pivote a 1 dividiendo toda la fila
        pivote = matriz[i][i]
        if pivote != 1 and pivote != 0:
            matriz[i] = [x / pivote for x in matriz[i]]
            mensaje = f"f{i + 1} -> f{i + 1}/{pivote}"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n")
            print("")
            mostrarMatriz(matriz)
        
        # Se eliminan los valores por debajo del pivote
        for j in range(i + 1, filas):
            if matriz[j][i] != 0:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(columnas)]
                mensaje = f"f{j + 1} -> f{j + 1} - {factor}f{i + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n")
                print("")
                mostrarMatriz(matriz)

    # Se elimina hacia atras para hacer la matriz identidad
    for i in range(filas - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if matriz[j][i] != 0:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(columnas)]
                mensaje = f"f{j + 1} -> f{j + 1} - {factor}f{i + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n")
                print("")
                mostrarMatriz(matriz)

    # Verificar filas inconsistentes
    for fila in matriz:
        if all(x == 0 for x in fila[:-1]) and fila[-1] != 0:
            print("El sistema no tiene solución.")
            return None  # No hay solucion debido a inconsistencia

    return matriz
