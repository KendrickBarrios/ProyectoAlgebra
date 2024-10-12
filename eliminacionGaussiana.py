import matriz

from fractions import Fraction
def resolverMatriz(mat):
    filas = len(mat)
    columnas = len(mat[0])
    
    for i in range(filas):
        # Se encuentra el pivote y se intercambian las filas si es necesario
        if mat[i][i] == 0:
            for j in range(i + 1, filas):
                if mat[j][i] != 0:
                    mat[i], mat[j] = mat[j], mat[i]
                    mensaje = f"f{i + 1} <-> f{j + 1}"
                    print(mensaje)
                    print("-"*(len(mensaje) - 1), end=">\n")
                    print("")
                    matriz.mostrarMatriz(mat)
                    if esInconsistente(mat) is None:
                        return None
                    elif tieneInfinitas(mat):
                        matriz.mostrarInfinitas(mat)
                        return None
                    break
            else:
                continue  # Si no encuentra un pivote valido, pasa a la siguiente columna
        
        # Se convierte el pivote a 1 dividiendo toda la fila
        pivote = mat[i][i]
        if pivote != 1 and pivote != 0:
            mat[i] = [x / pivote for x in mat[i]]
            mensaje = f"f{i + 1} -> f{i + 1}/({pivote})"
            print(mensaje)
            print("-"*(len(mensaje) - 1), end=">\n")
            print("")
            matriz.mostrarMatriz(mat)
        
        # Se eliminan los valores por debajo del pivote
        for j in range(i + 1, filas):
            if mat[j][i] != 0:
                factor = mat[j][i]
                mat[j] = [mat[j][k] - factor * mat[i][k] for k in range(columnas)]
                mensaje = f"f{j + 1} -> f{j + 1} - ({factor})f{i + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n")
                print("")
                matriz.mostrarMatriz(mat)
                if esInconsistente(mat) is None:
                    return None

    # Se elimina hacia atras para hacer la matriz identidad
    for i in range(filas - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if mat[j][i] != 0:
                factor = mat[j][i]
                mat[j] = [mat[j][k] - factor * mat[i][k] for k in range(columnas)]
                mensaje = f"f{j + 1} -> f{j + 1} - ({factor})f{i + 1}"
                print(mensaje)
                print("-"*(len(mensaje) - 1), end=">\n")
                print("")
                matriz.mostrarMatriz(mat)
                if esInconsistente(mat) is None:
                    return None
                elif tieneInfinitas(mat):
                    matriz.mostrarInfinitas(mat)
                    return None

    return mat

def esInconsistente(mat):
    # Verificar filas inconsistentes
    for fila in mat:
        if all(x == 0 for x in fila[:-1]) and fila[-1] != 0:
            print("El sistema no tiene solución.")
            return None  # No hay solucion debido a inconsistencia
    return mat

def tieneInfinitas(mat):
    for fila in mat:
        if all(x == 0 for x in fila):
            return True