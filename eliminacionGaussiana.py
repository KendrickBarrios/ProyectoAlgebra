from fractions import Fraction

def mostrarMatriz(matriz):
    for fila in matriz:
        print('  '.join(str(x) for x in fila))
    print()

def resolverMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        # Encontrar el pivote y hacer el intercambio de filas si es necesario
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
                continue  # Si no encuentra un pivote válido, pasa a la siguiente columna
        
        # Convertir el pivote a 1 dividiendo toda la fila
        pivote = matriz[i][i]
        if pivote != 1 and pivote != 0:
            matriz[i] = [x / pivote for x in matriz[i]]
            mensaje = f"f{i + 1} -> f{i + 1}/{pivote}"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n")
            print("")
            mostrarMatriz(matriz)
        
        # Eliminar los valores por debajo del pivote
        for j in range(i + 1, filas):
            if matriz[j][i] != 0:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(columnas)]
                mensaje = f"f{j + 1} -> f{j + 1} - {factor}f{i + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n")
                print("")
                mostrarMatriz(matriz)

    # Eliminación hacia atrás para hacer la matriz diagonal
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
            return None  # No hay solución debido a inconsistencia

    return matriz
